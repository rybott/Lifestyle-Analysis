from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def main(request):
    pass

def login_employee(request):
    return render(request,'login.html',{})
