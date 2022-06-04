from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import RegisterForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()
    return render(request,'register/register.html', {"form":form})