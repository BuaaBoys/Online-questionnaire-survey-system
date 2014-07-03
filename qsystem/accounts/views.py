from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def register(request):
	return HttpResponse("Hi!")
