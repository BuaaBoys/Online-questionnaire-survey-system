from django.db import models
from django.forms import ModelForm
<<<<<<< HEAD
from datetime import datetime
=======
>>>>>>> Deploy static dir

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 20)
	sex = models.CharField(max_length = 6, null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	registered = models.NullBooleanField()
<<<<<<< HEAD
	register_date = models.DateTimeField(null=True, blank=True, default=datetime.now())
=======
	register_date = models.DateField(null=True, blank=True)
>>>>>>> Deploy static dir
	def __unicode__(self):
		return "E-mail:" + self.email

class UserForm(ModelForm):
	class Meta:
		model = User
<<<<<<< HEAD
		fields = ['email', 'password', 'sex', 'birthday', 'registered']
=======
		fields = ['email', 'password', 'birthday']
>>>>>>> Deploy static dir
