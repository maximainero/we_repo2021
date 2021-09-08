from django.contrib import auth
from .models import *
from django.shortcuts import render, redirect
from sitio.forms import FormCreateUser, FormLogin, FormCreateArticle
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.views.generic import View

## TOKEN AUTH USER
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse
from .tokenizer import token_generator

def home(request): #Pagina principal
    articles = Article.objects.all()
    content = {}
    sender = []
    for article in articles:
        content = {
            'title': article.title,
            'date_created': article.date_created,
            'link': '/articulo/' + str(article.id),
            'user': article.user,
            'image': article.image_one.url,
        }
        sender.append(content)
    return render(request, 'home.html', {'articles': sender})

def logear(request): #Logeo de usuarios ya creados
    if not request.user.is_authenticated: # Check if its ok
        form = FormLogin()
        no_activo = False
        mensajes = []
        if request.method == "POST":
            form = FormLogin(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        next = request.POST.get('next')
                        if next:
                            return redirect(request.POST.get('next'))
                        return redirect('homepage')
            else:
                username = form.cleaned_data['username']     
                usuarios_comunes = User.objects.all()
                usuario_encontrado = False
                for usr in usuarios_comunes:
                    if (usr.username == username): 
                        usuario_encontrado = True
                        break
                if (usuario_encontrado):
                    if (not usr.is_active):
                        mensajes.append('El usuario no está activo, verifique su email')
                    else:
                        mensajes.append('La contraseña ingresada es incorrecta') 
                else:
                    msj = 'El usuario "' + username + '" no existe'
                    mensajes.append(msj)        
        context = {'form': form, 'messages': mensajes}
        return render(request, "login.html", context)
    else:
        return redirect('homepage')

def crear_usuario(request): #Registro de nuevo usuario
    if not request.user.is_authenticated: # Check if its ok
        mensajes = []
        if request.method == "POST":
            form = FormCreateUser(data=request.POST)
            if form.is_valid():
                validar_mail = request.POST['email']
                lista_usuarios = User.objects.all() #Se trae todos los usuarios que haya para validar mail existente
                email_valido = True
                for u in lista_usuarios:
                    if u.email == validar_mail:
                        email_valido = False
                        break
                if email_valido:
                    user = form.save()
                    user.is_active = False
                    grupo = Group.objects.get(name = 'comun')
                    user.groups.add(grupo)
                    Profile.objects.create(
                        user = user
                    )

                    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                    domain = get_current_site(request).domain
                    link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
                    
                    activate_url = 'http://'+domain+link
                    user.save()
                    email = EmailMessage(
                        'Hola ' +user.username+ '! Gracias por registrarte!',
                        'Activa tu cuenta mediante este link: '+ activate_url,
                        'validate.canjea@gmail.com',
                        [user.email]
                    )
                    email.send(fail_silently=False)

                    return redirect('login')
                else:
                    mensajes.append('El mail ingresado ya existe')    
        else:
            form = FormCreateUser()
        context = {'form': form, 'messages': mensajes}   
        return render(request, 'crear_usuario.html', context)
    else:
        return redirect('homepage')


@login_required(login_url='login') #Pide el logeo de un usuario para poder ingresar a una pagina en espesifico
def mis_articulos(request):
    articles = Article.objects.all().filter(user = request.user)
    content = {}
    sender = []
    for article in articles:
        content = {
            'title': article.title,
            'date_created': article.date_created,
            'link': '/articulo/' + str(article.id),
            'image': article.image_one.url,
        }
        sender.append(content)
    return render(request, 'mis_articulos.html', {'articles': sender})

@login_required()
def cargar_articulo(request):
    mensajes = []
    if request.method == "POST":
        form = FormCreateArticle(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user = request.user
            new_article.save()
            return redirect('mis_articulos')
    else:
        form = FormCreateArticle()
    context = {'form': form, 'messages': mensajes} 
    return render(request, 'cargar_articulo.html', context)

@login_required(login_url='login') #Pide el logeo de un usuario para poder ingresar a una pagina en espesifico
def mis_canjes(request):
    return render(request, 'mis_canjes.html')

@login_required()
def cargar_canje(request):
    return render(request, 'cargar_canje.html')

@login_required(login_url='homepage') #Pide el logeo de un usuario para poder ingresar a una pagina en espesifico
def logout(request):
    auth.logout(request)
    return redirect("homepage")

def article(request, id):
    article = Article.objects.get(pk=id)
    if article:
        return render(request, 'articulo.html', {'article': article})
    else:
        pass


class verificationview(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login')

            if user.is_active:
                return redirect('homepage')
            user.is_active = True
            user.save()

            messages.success(request, 'Usuario activado con Éxito')
            return redirect('login')
        except Exception as ex:
            pass
            return redirect('login')