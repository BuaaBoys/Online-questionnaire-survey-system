from django.contrib import admin
from accounts.models import User
from investmanager.models import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    fields=['title','subject','description']
    list_display = ('title','subject','description')

admin.site.register(User)
admin.site.register(Questionnaire, QuestionnaireAdmin)
