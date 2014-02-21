from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'beancup.views.home', name='bean_home'),
    url(r'^beanblog/', include('beanblog.urls'), name='bean_blog'),
    url(r'^beanvote/', include('votebean.urls'), name='bean_votes'),
    url(r'^beanbrew/', include('beanbrew.urls'), name='bean_brew'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'beancup.views.bean_login', name='bean_login'),
    url(r'^logout/', 'beancup.views.bean_logout', name='bean_logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^register/', 'beancup.views.bean_register', name='bean_register'),
    url(r'^accounts/profile/$', 'beancup.views.profile', name='bean_profile'),

)
