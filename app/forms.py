from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class RegistrarCuenta(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name','password1','password2']

class RegistrarUsuario(ModelForm):
	class Meta:
		model = Usuario
		fields = ['carnet','nombres','correo_institucional','apellidos','numero_contacto','id_facultad']