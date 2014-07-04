#-- coding:utf-8 --
'''Process all requests relatived to questionnaire

include TODO and publish'''

import datetime
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,render_to_response

from accounts.models import User

from models import Questionnaire
from form import QuestForm
from questions import *

def show_quest_fill_page(request):
	'''let investigator create the questionnaire'''

	return render_to_response("investmanager/4_5.html", {})


def publish(request):
	'''pass basic infomation to next page

	when the button is pressed, the arguments will be passed.'''

	form = QuestForm(request.POST)
	if form.is_valid():
		quest = form.save()
                try:
                        questions = Questions(qid=str(quest.id))
                        questionTitles = request.POST.getlist('question')
                        questionTypes = request.POST.getlist('type')
                        # 根据post的信息构造Question，将Question加入Questions
                        # 太丑了救命
                        for i, qtitle in enumerate(questionTitles):
                                qtype = questionTypes[i]
                                qitems = []
                                if qtype == "single" or qtype == "multiply":
                                        value = 'items' + str(i)
                                        qitems = request.POST.getlist(value)
                                        print qtitle, qtype, qitems
                                        question = Question(qtype, qtitle, qitems)
                                        questions.addQuestion(question)
                        questions.write()
                except Exception, e:
                        print e
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
