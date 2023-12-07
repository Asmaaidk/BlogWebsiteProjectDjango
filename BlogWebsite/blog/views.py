from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Post, Category, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

def blogs(request):
  blogs = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'blogs': blogs,
  }
  return HttpResponse(template.render(context, request))


def users(request):
  users = User.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))

def comments(request):
  comments = Comment.objects.all().values()
  template = loader.get_template('comments.html')
  context = {
    'comments': comments,
  }
  return HttpResponse(template.render(context, request))

def categories(request):
  categories = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'categories': categories,
  }
  return HttpResponse(template.render(context, request))

def blogdetails(request,id):
  blogs = Post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'blogs': blogs,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())