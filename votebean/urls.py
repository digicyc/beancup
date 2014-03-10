from django.conf.urls import patterns, url

urlpatterns = patterns('votebean.views',
    url(r'^$', 'home', name='votebean_home'),
    url(r'add_vote/$', 'add_vote', name='add_vote'),
)