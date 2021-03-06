from django.conf.urls import patterns, url
from investmanager.models import Questionnaire
from django.core.urlresolvers import reverse
from django.shortcuts import render

def home(request):
	released_questionnaires = Questionnaire.objects.filter(released=True, anonymous_limit=False)
	# TODO judge length
	slicelen = len(released_questionnaires)
	if slicelen > 10:
		return render(request, "homepage/index.html", {"released_quest":released_questionnaires[(slicelen-10):slicelen]})
	else:
		return render(request, "homepage/index.html", {"released_quest":released_questionnaires})
	
def message(request, msg):
	if msg == "loggedin":
		message = AlertMessage("success", "Success!", " You are logged in now.", "/")
	if msg == "loggedout":
		message = AlertMessage("success", "Success!", " You are logged out now.", "/")
	if msg == "registered":
		message = AlertMessage("success", "Success!", " You are signed up, log in and see what you can do.", "/accounts/login")
	if msg == "loginfirst":
		message = AlertMessage("info", "Please log in first.", " You are not allowed to view current page.", "/accounts/login")
	if msg == "errorpage":
		message = AlertMessage("warning", "Forbid.", " You are not allowed to view current page.", reverse('home'))
	return render(request, "homepage/message.html", {"message": message,})


class AlertMessage():
	def __init__(self, alert_type, message_strong, message_content, redirect_target):
		self.alert_type = alert_type
		self.message_strong = message_strong
		self.message_content = message_content
		self.redirect_target = redirect_target
	def __str__(self):
		return self.message_content
