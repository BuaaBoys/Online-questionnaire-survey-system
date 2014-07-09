'''Url request dispatcher'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^(\d{1,})$', views.quest),
		url(r'^publish$', views.publish),
		url(r'^published$', views.published),
		url(r'^draft$', views.draft),
		url(r'^$', views.show_quest_fill_page),
		url(r'^home$', views.manage_all),
		url(r'^filled/(?P<page>\d{1,})$', views.manage_filled),
		)
