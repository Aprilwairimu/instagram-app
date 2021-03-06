from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class LoginForm(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class UploadImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ("image","image_name","image_caption")

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ("author","comment","image")
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'comment':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
            }