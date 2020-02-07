from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Django says Hey there partner!<a href="/rango/about">About</a>')

def about(request):
    return HttpResponse('Rango says here is the about page<a href="/rango">Home</a>')