from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import User

class UserForms(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','CPF','Phone','username','password','cep','bairro','cidade','estado','rua','numero','complemento','cnpj')