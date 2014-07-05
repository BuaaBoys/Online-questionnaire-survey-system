from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from results.models import Result
from investmanager.models import Questionnaire 
import xml.dom.minidom
from results.questions.questions import Questions


def answer(request, qid):
	try:
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		Naire.read()
		#Naire.write()
		q = get_object_or_404(Questionnaire, pk=qid)
		return render(request, 'results/answer.html' ,{'Questionnaire':q ,'naire':Naire ,'qid':qid})
	except:
		return render(request, 'results/error404.html')

def publish(request, qid):
	try:
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		Naire.read()
		result = ''
		for x in xrange(1,Naire.count+1):
			if Naire.questionList[x-1].qtype == 'single':
				result += request.POST[str(x)] + ','
			elif Naire.questionList[x-1].qtype == 'multiply':
				rlist = request.REQUEST.getlist(str(x))
				if len(rlist)==0:
					raise Exception()
				m = '['
				for r in rlist:
					m += r + ','
				m += '],'
				result += m
			elif Naire.questionList[x-1].qtype == 'truefalse':
				result += request.POST[str(x)] + ','
			elif Naire.questionList[x-1].qtype == 'essay':
				result += request.POST[str(x)] + ','

		user = "anonymity@admin.com"
		user = request.COOKIES.get("email")
		if user == None:
			user = "anonymity@admin.com"
		r = Result(questionnaire_id=qid,participant_id=user,answer=result)
		r.save()
		return render(request, 'results/success.html')
	except:
		q = get_object_or_404(Questionnaire, pk=qid)
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		Naire.read()
		return render(request, 'results/answer.html',{'Questionnaire':q ,'naire':Naire ,'qid':qid, 'errorMsg':'Not finished yet!'})	
		
def success(request):
	return render(request, 'success.html')

def error404(request):
	try:
		Naire = Questions()
		Naire.qid = qid 
		Naire.read()
		q = get_object_or_404(Questionnaire, pk=qid)
		return render(request, 'results/answer.html' ,{'Questionnaire':q ,'naire':Naire ,'qid':qid})
	except:
		return render(request, 'results/error404.html')
