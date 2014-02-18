from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'beancup.views.home', name='home'),
    url(r'^beanblog/', include('beanblog.urls')),
    url(r'^beanvote/', include('votebean.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'beancup.views.bean_login', name='bean_login'),
    url(r'^logout/', 'beancup.views.bean_logout', name='bean_logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),

)
