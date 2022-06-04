from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,UploadImageForm
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

def profile(request):
    profile = profile.objects.all()
    return render(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.success(request,('picture posted'))
            return render(request,'post.html',{"form":form})

def comment(request):
    comment = comment.objects.all()
    return render(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.success(request,('comment posted'))
            return render(request,'home.html',{"post":post})


