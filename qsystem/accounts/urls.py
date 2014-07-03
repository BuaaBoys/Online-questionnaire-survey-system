from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
	url(r'^register/$', views.register, name = 'register'),
	url(r'^register/submit/$', views.register_submit, name = 'register_submit'),
<<<<<<< HEAD
	url(r'^login/$', vies.login, name = 'login'),
	url(r'^login/submit/$', vies.login_submit, name = 'login'),
=======
>>>>>>> Deploy static dir
)		