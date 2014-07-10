'''Url request dispatcher'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^(\d{1,})$', views.quest),
		url(r'^publish$', views.publish, name="publish"),
		url(r'^create$', views.show_quest_fill_page, name='create'),
		url(r'^modify/(?P<no>\d{1,})$', views.modify_quest, name='modify'),
		url(r'^resave/(?P<no>\d{1,})$', views.resave_quest, name='resave'),
		url(r'^$', views.redirect_to_home),
		url(r'^home$', views.manage_all, name='home'),
		url(r'^(?P<type>[a-z]{1,})/(?P<page>\d{1,})$', views.manage_dashboard, name='dashboard'),
		url(r'toggle/(?P<action>[a-z]{1,})/(?P<no>\d{1,})', views.toggle_state, name='toggle'),
		)
