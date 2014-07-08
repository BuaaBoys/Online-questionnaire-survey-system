from django.db import models

class Result(models.Model):
	questionnaire_id = models.BigIntegerField()
	participant_id = models.TextField()
	answer = models.TextField()

