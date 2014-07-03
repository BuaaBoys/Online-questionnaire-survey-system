from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from accounts.models import User, UserForm
<<<<<<< HEAD
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

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
		is_error = "hidden"
		error_msg = ""
		return render(request, 'accounts/register.html', {"error_msg":error_msg, "is_error":is_error})
	is_error = ""
	error_msg = "Existed E-mail Address"
	return render(request, 'accounts/register.html', {"error_msg":error_msg, "is_error":is_error})

def login(request):
	is_error = False
	error_msg = ""
	return(request, "accounts/login.html",{"error_msg":error_msg, "is_error":is_error})

def login_submit(request):
	try:
		user = User.objects.get(email=request.POST['email'])
	except:
		is_error = True
		error_msg = "E-mail does not exist"
		return render(request, "accounts/login.html", {"error_msg":error_msg, "is_error":is_error})
	if user.password == request.POST['password']:
		


=======

def register(request):
	return render(request, 'accounts/register.html', None)

def register_submit(request):
	# u = User(email = request.POST['email'], password = request.POST['password'], sex = request.POST['sex'])
	'''
	u = User()
	u.email =  request.POST['email']
	u.password = request.POST['password']
	u.sex = request.POST['sex']
	u.save()
	'''
	form = UserForm(request.POST)
	form.save()
	return render(request, 'accounts/register.html', None)
>>>>>>> Deploy static dir
