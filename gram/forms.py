
from djando.contrib.auth import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = models.EmailFeild()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]