from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import UpdateView
from .models import User
from django.contrib.auth import authenticate
from django.views.generic import CreateView
from django.contrib.auth import login
from app.forms import SignUpForm

# Create your views here.

def index(request):
    users =User.objects.all()
    return render(request,'app/home.html',{'users':users})


def detail(request,id):
    user = User.objects.get(pk=id)

    return render(request,'app/detail.html',{'publisher':user})

def top(request):
    return render(request,'app/top.html')

class DeviceUpdateView(UpdateView):
    fields = ('name','url','image', 'device','controller','sound','memo')
    model = User
