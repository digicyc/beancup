from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'beancup.views.home', name='home'),
    url(r'^beanblog/', include('beanblog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
