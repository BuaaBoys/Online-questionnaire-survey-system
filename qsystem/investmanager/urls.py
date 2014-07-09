'''Url request dispatcher'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^(\d{1,})$', views.quest),
		url(r'^publish$', views.publish),
		#url(r'^published/(?P<page>\d{1,})$', views.published, name='published'),
		#url(r'^draft/(?P<page>\d{1,})$', views.draft, name='draft'),
		url(r'^$', views.show_quest_fill_page),
		url(r'^home$', views.manage_all),
		url(r'^filled/(?P<page>\d{1,})$', views.manage_filled),
		url(r'^(?P<type>[a-z]{1,})/(?P<page>\d{1,})$', views.manage_cao, name='cao')
		)
