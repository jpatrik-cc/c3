from django.conf.urls.defaults import *

urlpatterns = patterns('cococloud.discovery.views',
    url(r'^$', 'local_options', name='discovery_areas'),
)
