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
	'''let investigator create the questionnaire'''

	return render_to_response("investmanager/4.html", {})


def publish(request):
	'''pass basic infomation to next page

	when the button is pressed, the arguments will be passed.'''

	form = QuestForm(request.POST)
	if form.is_valid():
		quest = form.save(request)

		# this place manage the content to xml conversion, use the id which database automatic generate
		return HttpResponseRedirect(str(quest.id))


def quest(request, no):
	'''let people fill the questionnaire'''

	try:
		no = int(no)
		quest = Questionnaire.objects.get(id=no)
	except:
		raise Http404()

	id = quest.id
	title = quest.title
	subject = quest.subject
	description = quest.description

	return render_to_response("investmanager/show_quest.html",{'id':id, "title":title, "subject":subject, "description":description,})
