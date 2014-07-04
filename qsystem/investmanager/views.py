#-- coding:utf-8 --
'''Process all requests relatived to questionnaire

include TODO and publish'''

import datetime
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,render_to_response

from accounts.models import User

from models import Questionnaire
from form import QuestForm

def show_quest_fill_page(request):
	return render(request, "investmanager/4.html", {})

def publish(request):
	'''pass basic infomation to next page

	when the button is pressed, the arguments will be passed.'''

	form = QuestForm(request.POST)
	form.save()
	# this place manage the content to xml conversion, use the id which database automatic generate
	return HttpResponseRedirect("/")
