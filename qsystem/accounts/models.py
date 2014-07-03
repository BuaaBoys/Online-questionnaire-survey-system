from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 20)
	sex = models.CharField(max_length = 6)
	birthday = models.DateField()
	registered = models.BooleanField()
	register_date = models.DateField()
	def __unicode__(self):
		return "E-mail:" + self.email