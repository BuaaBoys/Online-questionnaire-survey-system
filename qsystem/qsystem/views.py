from django.conf.urls import patterns, url
from django.shortcuts import render

def home(request):
	return render(request, "homepage/index.html")