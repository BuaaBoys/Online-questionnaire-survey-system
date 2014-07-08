from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User, UserForm
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
import urllib
from accounts.authentication import Authentication

def register(request):
	is_error = "hidden"
	error_msg = ""
	return render(request, 'accounts/register.html', {"error_msg":error_msg, "is_error":is_error})

def register_submit(request):
	try:
		User.objects.get(email=request.POST['email'])
	except:
		form = UserForm(request.POST)
		form.save()
		response = HttpResponseRedirect("/message/registered")
		return response
	is_error = ""
	error_msg = "Existed E-mail Address"
	return render(request, 'accounts/register.html', {"error_msg":error_msg, "is_error":is_error})

def login(request):
	is_error = "hidden"
	error_msg = ""
	return render(request, "accounts/login.html",{"error_msg":error_msg, "is_error":is_error})

def login_submit(request):
	try:
		user = User.objects.get(email=request.POST['email'])
	except:
		is_error = ""
		error_msg = "E-mail does not exist"
		return render(request, "accounts/login.html", {"error_msg":error_msg, "is_error":is_error})
	user_auth = Authentication(request)
	if user.password == request.POST['password']:
		response = HttpResponseRedirect("/message/loggedin")
		user_auth.set_cookie(response, user)
		return response
	else:
		is_error = ""
		error_msg = "Password not matching"
		return render(request, "accounts/login.html", {"error_msg":error_msg, "is_error":is_error})

