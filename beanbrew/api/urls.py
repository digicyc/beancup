from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('beanbrew.api.views',
    url(r'brews', 'brews', name='brews'),
)

urlpatterns = format_suffix_patterns(urlpatterns)