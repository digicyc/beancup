from django.conf.urls import patterns, url
from beanbrew.views import BrewView

urlpatterns = patterns('',
    url(r'^$', 'beanbrew.views.home', name='beanbrew_home'),
    url(r'^add_brew/', BrewView.as_view(), name='add_brew'),
)