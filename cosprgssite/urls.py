from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cosprgssite.views.home', name='home'),
    url(r"^accounts/login/$", login),
    url(r"^accounts/logout/$", logout),
    url(r"^accounts/profile/$","cosprgssite.Friends.views.display_profile"),
    url(r'^committees/', include('cosprgssite.committees.urls')),
    url(r'^Friends/',include('cosprgssite.Friends.urls')),
    url(r'^history/', include('cosprgssite.history.urls')),
    url(r'^meetings/', include('cosprgssite.meetings.urls')),
    url(r'^testimonies/', include('cosprgssite.testimonies.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
