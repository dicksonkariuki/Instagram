from django.shortcuts import render,redirect,get_object_or_404
from .models import Comment,Image,Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from.forms import ProfileForm,ImageForm,CommentForm
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request,'welcome.html')

# Create your views here.
