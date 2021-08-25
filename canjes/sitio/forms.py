from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

"""from django.forms import models
from django.forms.fields import DateField, DateTimeField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import Widget"""

"""class FormCreateUser(forms.Form): #Lista de datos que se necesitan al crear un usuario nuevo
    name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    lastname = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    email = forms.EmailField(label="", max_length=125, widget=forms.TextInput(attrs={'placeholder':'E-Mail'}))
    location = forms.CharField(label="", max_length=125, widget=forms.TextInput(attrs={'placeholder':'Localidad'}))
    cp = forms.CharField(label="", max_length=4, widget=forms.TextInput(attrs={'placeholder':'Codigo Postal'}))
    fecha_nacimiento = forms.DateField(label="", widget=forms.DateInput(attrs={'type':'date'}))
    cuil_cuit = forms.CharField(label="", max_length=10, widget=forms.TextInput(attrs={'placeholder':'CUIT/CUIL'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Nueva Contraseña'}))
    password_checks = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Repetir Contraseña'}))

    def clean_name(self): #Controla que no se ingrtesen malas palabras en el nombre
        malas_palabras = ['maldito', 'maldita', 'puto', 'puta', 'idiota', 'imbecil', 'nazi', 'pelotudo', 'pelotuda', 'boludo', 'boluda']
        texto_ingresado = self.cleaned_data['name']
        for i in malas_palabras:
            if texto_ingresado in malas_palabras:
                raise ValidationError("No se puede ingresar malas palabras")
            break
        return texto_ingresado

    def clean_lastname(self): #Controla que no se ingrtesen malas palabras en el apellido
        malas_palabras = ['maldito', 'maldita', 'puto', 'puta', 'idiota', 'imbecil', 'nazi', 'pelotudo', 'pelotuda', 'boludo', 'boluda']
        texto_ingresado = self.cleaned_data['lastname']
        for i in malas_palabras:
            if texto_ingresado in malas_palabras:
                raise ValidationError("No se puede ingresar malas palabras")
            break
        return texto_ingresado
    
    def clean_location(self): #Controla que no se ingrtesen malas palabras en la localidad
        malas_palabras = ['maldito', 'maldita', 'puto', 'puta', 'idiota', 'imbecil', 'nazi', 'pelotudo', 'pelotuda', 'boludo', 'boluda']
        texto_ingresado = self.cleaned_data['location']
        for i in malas_palabras:
            if texto_ingresado in malas_palabras:
                raise ValidationError("No se puede ingresar malas palabras")
            break
        return texto_ingresado

    def clean_cp(self): #Controla que solo se ingresen numeros en el codigo postal
        numeros = {'0','1','2','3','4','5','6','7','8','9'}
        codpos = self.cleaned_data['cp']
        for x in codpos:
            if x not in numeros:
                raise forms.ValidationError('El codigo postal solo admite numeros')
    
    def clean_cuil_cuit(self): #Controla que solo se ingresen numeros en el cuil/cuit
        numeros = {'0','1','2','3','4','5','6','7','8','9'}
        codpos = self.cleaned_data['cuil_cuit']
        for x in codpos:
            if x not in numeros:
                raise forms.ValidationError('El cuil/cuit solo admite numeros')

    def clean_password_checks(self): #Controla que las 2 contraseñas coinsidan
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password_checks']
        if pass1 != pass2:
            raise forms.ValidationError('La contraseña no coincide')
        return pass2"""

class FormCreateUser(UserCreationForm):
    first_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    email = forms.EmailField(label="", max_length=125, widget=forms.TextInput(attrs={'placeholder':'E-Mail'}))
    username = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2']
        help_texts = {
            'first_name': None,
            'last_name': None,
            'email': None,
            'username': None,
        }
    
    def __init__(self,*args,**kwargs):
        super(FormCreateUser, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['password1'].label = ''      
        self.fields['password1'].help_text = ''        

        self.fields['password2'].widget.attrs['placeholder'] = "Confirmar contraseña"
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

class FormLogin(AuthenticationForm):
    def confirm_login_allowed(self, user): # Bypass login without is_active() 
        pass

    def __init__(self,*args,**kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = "Usuario"
        self.fields['username'].label = ''

        self.fields['password'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['password'].label = ''  

"""class FormLogin(forms.Form): #Lista de datos para logear
    email = forms.EmailField(label="", max_length=125, widget=forms.TextInput(attrs={'placeholder':'E-Mail'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
"""
class FormRecuperarContraseña(forms.Form): #Lista de datos pararecuperar contraseña
    email = forms.EmailField(label="", max_length=125, widget=forms.TextInput(attrs={'placeholder':'E-Mail'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Nueva Contraseña'}))
    password_checks = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Repetir Contraseña'}))

