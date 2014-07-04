from django.contrib import admin
from accounts.models import User
from investmanager.models import Questionnaire

admin.site.register(User)
admin.site.register(Questionnaire)
