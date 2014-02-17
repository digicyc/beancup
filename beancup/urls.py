from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('beancup.views',
    url(r'^$', 'home', name='home'),
    url(r'^beanblog/', include('beanblog.urls')),
    url(r'^beanvote/', include('votebean.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'bean_login', name='bean_login'),
    url(r'^logout/', 'bean_logout', name='bean_logout'),
)
