from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.contrib import admin


class UsuarioManager(BaseUserManager):

    def create_user(self, username, nombre, apellido, password):
        if not nombre:
            raise ValidationError('El usuario debe tener nombre')
        elif not apellido:
            raise ValidationError('El usuario debe tener apellido')

        usuario = self.model(
            username = username,
            nombre = nombre,
            apellido = apellido,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, nombre, apellido, password):
        usuario = self.create_user(

            username = username,
            nombre = nombre,
            apellido = apellido,
            password = password
        )
        usuario.usuario_admin = True
        usuario.save()
        return usuario



class usuario(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=30)
    nombre = models.CharField(max_length= 30, null=False)
    apellido = models.CharField(max_length=30, null= False)
    is_active = models.BooleanField(default=True)
    usuario_admin= models.BooleanField(default=False)
    object = UsuarioManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    def __str__(self):
        return f'{self.username}, {self.nombre}'

    def has_perm(self,perm,obj = None):
        return True
    def has_perms(self, perm, obj= None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_admin



    class Meta:
        db_table = 'Usuario'
         

