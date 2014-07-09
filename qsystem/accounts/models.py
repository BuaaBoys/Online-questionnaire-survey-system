from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 20)
	sex = models.CharField(max_length = 6, null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	registered = models.NullBooleanField()
	register_date = models.DateTimeField(null=True, blank=True, default=datetime.now())
	def __unicode__(self):
		return self.email

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password', 'sex', 'birthday', 'registered']

