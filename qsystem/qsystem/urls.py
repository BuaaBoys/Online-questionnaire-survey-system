from django.conf.urls import patterns, include, url
from accounts.views import register

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qsystem.views.home', name='home'),
    # url(r'^qsystem/', include('qsystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/register/', register, name = 'register'),
    url(r'^quest/', include('investmanager.urls')),
)
