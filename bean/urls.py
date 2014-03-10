from django.conf.urls import patterns, url
from .views import BeanView

urlpatterns = patterns('',
    url(r'^add_bean/', BeanView.as_view(), name='add_bean'),
)
