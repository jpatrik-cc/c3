from django.conf.urls.defaults import *

urlpatterns = patterns('cococloud.discovery.views',
    (r'^$', 'point'),
)
