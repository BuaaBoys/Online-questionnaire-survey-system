from django.db import models

class Result(models.Model):
	questionnaire_id = models.BigIntegerField()
	participant_id = models.EmailField()
	answer = models.TextField()

