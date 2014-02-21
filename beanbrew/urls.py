from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'beanbrew.views.home', name='beanbrew_home'),
)