from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,LoginForm,UploadImageForm,CommentForm
from urllib import request
from .models import *
# Create your views here.

def home(request):
    posts = Image.objects.all()
    form = CommentForm
    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request,'home.html',{"posts":posts,"form":form})

def logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()
    return render(request,'register/register.html', {"form":form})

def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=usern,password=passw)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    return render(request,'register/login.html',{'form':form})

def profile(request):
    profile = profile.objects.all()
    return render(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.success(request,('picture posted'))
            return render(request,'post.html',{"form":form})

def post_pic(request):
    form = UploadImageForm(request.POST,request.FILES)
    profile = Profile.objects.all()
    if request.method =='POST':
        if form.is_valid():
            form.save()
        messages.success(request,('picture posted'))
    return render(request,'post.html',{"form":form,"profile":profile})

def ViewImage(request, pk):
    post = get_object_or_404(Image, id=pk)
    image = Image.objects.get(id=pk)
    total_likes = stuff.total_likes()

    return render(request, 'image.html', {'image': image, 'post': post, 'total_likes': 
    total_likes})

def comment(request):
    comment = comment.objects.all()
    return render(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.success(request,('comment posted'))
            return render(request,'home.html',{"post":post})

def like(request, pk):
    post = get_object_or_404(Image, id=request.GET.get('post_id'))
    post.Likes.add(request.user)   

    return HttpResponseRedirect(reverse('view', args=[str(pk)]))


def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_username = Username.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"usernames": searched_usernames})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
