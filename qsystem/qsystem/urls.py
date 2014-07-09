from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'qsystem.views.home', name='home'),
    url(r'^message/(?P<msg>[a-z]{1,})$', 'qsystem.views.message', name='message'),
    # url(r'^qsystem/', include('qsystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^quest/', include('investmanager.urls', namespace='quest')),
    url(r'^naire', include('results.urls', namespace='results')),
)
