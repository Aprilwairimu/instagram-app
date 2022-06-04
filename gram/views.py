from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from djando.contrib.auth import login,authenticate
from djando.contrib.auth import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = UserCreationForm()
    return render(request,'register/register.html', {"form":form})