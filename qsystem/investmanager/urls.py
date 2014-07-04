'''Url request dispatcher'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^publish$', views.publish),
		url(r'^$', views.show_quest_fill_page),
		)
