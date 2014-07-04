# --coding: utf-8 --
from django.forms import ModelForm

from accounts.models import User

from models import Questionnaire

class QuestForm(ModelForm):
	class Meta:
		model=Questionnaire
		fields=('title', 'subject', 'description',)

	def save(self, request):
		title = self.cleaned_data['title']
		subject = self.cleaned_data['subject']
		description = self.cleaned_data['description']
		#current_user_email = request.COOKIES.get("email")
		current_user_email = "kevin@kevin.com"
		current_user = User.objects.get(email=current_user_email)
		author = current_user

		return Questionnaire.objects.create(title=title, subject=subject, description=description, author=author)
