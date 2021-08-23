"""from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    USER = 1
    VIP = 2
    SUPERUSER = 3
    ROLE_CHOICES = (
        (USER, 'User'),
        (VIP, 'VIP'),
        (SUPERUSER, 'Superuser'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()"""

  
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 40, null = True)
    lastname = models.CharField(max_length = 40, null = True)
    location = models.CharField(max_length = 40, null = True)
    cp = models.IntegerField(max_length = 40, null = True)
    fecha_nacimiento = models.DateField(max_length = 40, null = True)
    cuil_cuit = models.CharField(max_length = 40, null = True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
