from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sklonyator.views.home', name='home'),
    url(r'^api', 'sklonyator.views.api', name='api'),
    url(r'^admin/', include(admin.site.urls)),
)
