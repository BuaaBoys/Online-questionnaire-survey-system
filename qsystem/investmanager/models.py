from django.db import models
from accounts.models import User

class Questionnaire(models.Model):
	'''Questionnaire model

	follow database design doc'''

	title = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	author = models.ForeignKey(User, related_name='Investigator')
	date = models.DateTimeField()
	closed = models.BooleanField()
