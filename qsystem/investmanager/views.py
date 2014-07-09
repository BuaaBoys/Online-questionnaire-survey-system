#-- coding:utf-8 --
'''Process all requests relatived to questionnaire

include TODO and publish'''

import datetime
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,render_to_response
from django.template import loader, RequestContext

from accounts.authentication import Authentication
from accounts.models import User

from models import Questionnaire
from form import QuestForm
from results.questions.questions import Question, Questions
from results.models import Result

from investmanager.context_processors import manage_proc
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def show_quest_fill_page(request):
	'''let investigator create the questionnaire'''
	auth = Authentication(request)
	if not auth.is_login():
		return HttpResponseRedirect("/message/loginfirst")
	return render(request, "investmanager/add_quest.html", {})

def publish(request):
	'''pass basic infomation to next page

	when the button is pressed, the arguments will be passed.'''

	for key in request.POST:
		print request.POST.getlist(key)
	questions = Questions()
	questions.clean()
	try:
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
			question = Question('', qtype, qtitle, qitems)
			questions.addQuestion(question)
	except Exception, e:
		print e
	form = QuestForm(request.POST, questions)
	if form.is_valid():
		quest = form.save(request)
		questions.clean()
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

	return render(request, "investmanager/show_quest.html",{"id":id, "title":title, "subject":subject, "description":description,})

def close_or_open(request):
	if request.method == "POST":
		if request.POST.has_key("reopen"):
			re = int(request.POST["reopen"])
			quest = Questionnaire.objects.filter(id = re)[0]
			quest.closed = False
			quest.save()

		elif request.POST.has_key("close"):
			re = int(request.POST["close"])
			quest = Questionnaire.objects.filter(id = re)[0]
			quest.closed = True
			quest.save()


def published(request):
	'''go to the published_quest page'''

	auth = Authentication(request)
	current_user = auth.get_user()
	#current_email = user.email

	quest_list = Questionnaire.objects.filter(author = current_user,released = True)

	close_or_open(request)

	context = RequestContext(request, {'quest_list':quest_list, 'quest_len':len(quest_list)}, processors = [manage_proc])
	return render(request, "investmanager/published_quest.html", context)

def draft(request):
	'''go to the draft_quest page'''

	auth = Authentication(request)
	current_user = auth.get_user()
	#current_email = user.email

	quest_list = Questionnaire.objects.filter(author = current_user, released = False)
	context = RequestContext(request, {'quest_list':quest_list,}, processors = [manage_proc])
	return render(request, "investmanager/draft_quest.html", context)

def manage_all(request):
	auth = Authentication(request)
	if not auth.is_login():
		return HttpResponseRedirect("/message/loginfirst")
	user = auth.get_user()
	pub_questionnaires = Questionnaire.objects.filter(author = user)
	results = Result.objects.filter(participant_id = user.email)

	close_or_open(request)

	created_quest = []
	created_num = 1
	filled_quest = []
	filled_num = 1

	for quest in pub_questionnaires:
		created_quest.append((created_num, quest.title, quest.closed,quest.id))
		created_num += 1
		if created_num >=5:
			break
	for result in results:
		quest = Questionnaire.objects.get(id = result.questionnaire_id)
		filled_quest.append((filled_num, quest.title, quest.closed))
		filled_num += 1
		if filled_num >= 5:
			break
	context = RequestContext(request, {"created_quest": created_quest, "filled_quest": filled_quest}, processors = [manage_proc])
	return render(request, "investmanager/index.html", context)
