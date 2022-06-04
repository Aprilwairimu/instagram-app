from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home',),
     path('Register',views.register, name='register',),
]