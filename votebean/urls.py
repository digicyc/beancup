from django.conf.urls import patterns, include, url

urlpatterns = patterns('votebean.views',
    url(r'^$', 'home', name='votebean_home'),
)