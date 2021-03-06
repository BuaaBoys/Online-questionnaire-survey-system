# --coding: utf-8 --
from django.forms import ModelForm

from accounts.models import User

from models import Questionnaire

from accounts.authentication import Authentication

class QuestForm(ModelForm):
	class Meta:
		model=Questionnaire
		fields=('title', 'subject', 'description', )

	def __init__(self, post, questions):
		ModelForm.__init__(self, post)
		self.questions = questions

	def save(self, request):
		auth = Authentication(request)
		user = auth.get_user()
		title = self.cleaned_data['title']
		subject = self.cleaned_data['subject']
		description = self.cleaned_data['description']
		current_user_email = user.email
		contents = self.questions.build()
		current_user = User.objects.get(email=current_user_email)
		author = current_user
		
		released = False
		anonymous_limit = False
		if request.POST['input_action'] == "Publish Questionnaire":
			released = True
		if request.POST.has_key('anonymous_limit'):
			anonymous_limit = True
		#print released

		return Questionnaire.objects.create(title=title, subject=subject, description=description, contents=contents, author=author, released =released, anonymous_limit = anonymous_limit)
