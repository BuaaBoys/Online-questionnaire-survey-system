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
	form = QuestForm()
	return render(request, "4.html", {form:form, })

def publish(request):
	'''pass basic infomation to next page

	when the button is pressed, the arguments will be passed.'''

	if request.method == "POST":
		#form = QuestForm()
		if form.valid():
			f_title = form.cleaned_data["title"]
			f_subject = form.cleaned_data["subject"]
			f_description = form.cleaned_data["subject"]
			current_author = request.user
			questionnaire = Questionnaire(title=f_title, subject=f_subject, description=f_description, author=current_author, date=datetime.datetime.now(), closed=False)
			questionnaire.save()
			# this place manage the content to xml conversion, use the id which database automatic generate
	return HttpResponseRedirect("/")
