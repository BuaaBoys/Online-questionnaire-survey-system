from django.conf.urls import patterns,url
from results.models import Result
from results import views

urlpatterns = patterns('',
	url(r'^(?P<qid>\d+)$',views.answer),
	url(r'^(?P<qid>\d+)_$',views.publish),
	url(r'^success.html$',views.success)
	#url(r'^error404.html$',views.error404)
)
