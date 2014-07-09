from django.contrib import admin
from accounts.models import User
from investmanager.models import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('title','subject','description')
	list_filter = ['date']

admin.site.register(User)
admin.site.register(Questionnaire, QuestionnaireAdmin)
