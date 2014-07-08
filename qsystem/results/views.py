from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response
from investmanager.models import Questionnaire 
from qsystem.views import AlertMessage
from results.models import Result
from results.questions.questions import Questions


def answer(request, qid):
	try:
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		print 'questions:', len(Naire.questionList)
		q = get_object_or_404(Questionnaire, pk=qid)
		Naire.read(q.contents)
		print 'questions:', len(Naire.questionList)
		return render(request, 'results/answer.html' ,{'Questionnaire':q ,'naire':Naire ,'qid':qid})
	except:
		return render(request, "homepage/message.html", {"message": AlertMessage("danger", "Page 404!", "xxxx", "/"),})

def publish(request, qid):
	try:
		Naire = Questions()
		Naire.clean()
 		Naire.qid = qid
		Naire.read(get_object_or_404(Questionnaire, pk=qid).contents)
		result = []
		for x in xrange(1,Naire.count+1):
			if Naire.questionList[x-1].qtype == 'single':
				result.append([str(request.POST[str(x)])])
			elif Naire.questionList[x-1].qtype == 'multiply':
				rlist = request.REQUEST.getlist(str(x))
				if len(rlist)==0:
					raise Exception()
				m = []
				for r in rlist:
					m .append(r) 
				result.append(m)
			elif Naire.questionList[x-1].qtype == 'judge':
				result.append([str(request.POST[str(x)])])
			elif Naire.questionList[x-1].qtype == 'essay':
				if str(request.POST[str(x)]) !=  '' or str(request.POST[str(x)]) !=' ':
					result.append([str(request.POST[str(x)])])

		user = "anonymity@admin.com"
		user = request.COOKIES.get("email")
		if user == None:
			user = "anonymity@admin.com"
		r = Result(questionnaire_id=qid,participant_id=user,answer=str(result))
		print str(result)
		r.save()
		return render(request, "homepage/message.html", {"message": AlertMessage("success", "Success!", "You have already posted your answers", "/naire"+str(qid)+"/results"),})
	except:
		q = get_object_or_404(Questionnaire, pk=qid)
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		Naire.read(get_object_or_404(Questionnaire, pk=qid).contents)
		return render(request, 'results/answer.html',{'Questionnaire':q ,'naire':Naire ,'qid':qid, 'errorMsg':'Not finished yet!'})	
		
def success(request):
	return render(request, "homepage/message.html", {"message": AlertMessage("success", "Success!", "You have already posted your answers", "/results/results"),})

def error404(request):
	return render(request, "homepage/message.html", {"message": AlertMessage("danger", "Page 404!", "xxxx", "/"),})

def result(request, qid):
	try:
		Naire = Questions()
		Naire.clean()
		Naire.qid = qid
		Naire.read(get_object_or_404(Questionnaire, pk=qid).contents)
		q = get_object_or_404(Questionnaire, pk=qid)
		rts = Result.objects.filter(questionnaire_id=qid)
		
		# Start doing data collection
		# Dataset init
		dataset = []
		for x in xrange(1,Naire.count+1):
			if Naire.questionList[x-1].qtype == 'single':
				choice_set = []
				for x in xrange(0,len(Naire.questionList[x-1].items)):
					choice_set.append(0)
				dataset.append(choice_set)
			elif Naire.questionList[x-1].qtype == 'multiply':
				choice_set = []
				for x in xrange(0,len(Naire.questionList[x-1].items)):
					choice_set.append(0)
				dataset.append(choice_set)
			elif Naire.questionList[x-1].qtype == 'judge':
				choice_set = [ 0 , 0 ]
				dataset.append(choice_set)
			elif Naire.questionList[x-1].qtype == 'essay':
				dataset.append([])

		print dataset
		# ergodic
		count = 0
		for x in rts:
			simple_sheet = eval(x.answer)
			list_count = 0
			for l in simple_sheet:
				if Naire.questionList[list_count].qtype != 'essay':
					for i in l:
						dataset[list_count][int(i)-1] += 1
				elif Naire.questionList[list_count].qtype == 'essay':
					dataset[list_count] += l
				list_count += 1
			count += 1
		print dataset
		return render(request, 'results/results.html' ,{'Questionnaire':q ,'naire':Naire ,'qid':qid ,'result':dataset ,'count':count,})
	except:
		return render(request, "homepage/message.html", {"message": AlertMessage("danger", "Page 404!", "xxxx", "/"),})
