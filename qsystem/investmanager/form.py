# --coding: utf-8 --
from django.forms import ModelForm

from models import Questionnaire

class QuestForm(ModelForm):
	class Meta:
		model=Questionnaire
		fields=['title', 'subject', 'description']
