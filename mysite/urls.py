from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from mysite.books import views
admin.autodiscover()

urlpatterns = patterns('',
	# url> view, view > template!
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^display_meta/$', display_meta),
    url(r'^search/$', views.search),


)
