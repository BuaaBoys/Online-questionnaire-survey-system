import datetime
from django.db import models
from accounts.models import User

class Questionnaire(models.Model):
	'''Questionnaire model

	follow database design doc'''

	title = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	contents = models.TextField(default="None")
	author = models.ForeignKey(User, related_name='Investigator')
	date = models.DateTimeField(auto_now_add=True)
	closed = models.BooleanField(default=False)
	released = models.BooleanField(default=False)
	anonymous_limit = models.BooleanField(default=False)
	permitobjects_limit = models.TextField(default="[]")
	forbidobjects_limit = models.TextField(default="[]")

	def __unicode__(self):
		return self.title
