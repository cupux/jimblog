from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogArticle
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request,user)
            return render(request,'blog/index.html',{'blogs':blogs,'user':user} )
    return render(request,'blog/index.html',{'blogs':blogs,'user':None} )


def createBlog(request):
    blogs = BlogArticle.objects.all()
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.body = request.POST['body']
    newBlog.save()
    return render(request,'blog/index.html',{'blogs':blogs,'user':user} )
