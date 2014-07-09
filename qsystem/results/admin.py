from django.contrib import admin
from results.models import Result


class ResultAdmin(admin.ModelAdmin):
    fields=['questionnaire_id','participant_id','answer']
    list_display = ('questionnaire_id','participant_id','answer')
    list_filter = ['date']


admin.site.register(Result, ResultAdmin)
