from django.conf.urls import patterns,url
from results.models import Result
from results import views

urlpatterns = patterns('',
	url(r'^(?P<qid>\d+)$',views.answer ,name ='answer'),
	url(r'^(?P<qid>\d+)_$',views.publish ,name ='publish'),
	url(r'^(?P<qid>\d+)/results$',views.result ,name ='result')
)
