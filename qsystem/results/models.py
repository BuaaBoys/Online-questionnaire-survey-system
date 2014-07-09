from django.db import models
from investmanager.models import Questionnaire

class Result(models.Model):
	questionnaire_id = models.ForeignKey(Questionnaire, related_name='answer_sheet')
	participant_id = models.EmailField()
	answer = models.TextField()
	