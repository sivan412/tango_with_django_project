from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hi! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango About Page <br/> <a href='/rango/'>Index</a>")
