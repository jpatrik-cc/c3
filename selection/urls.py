from django.conf.urls.defaults import *

urlpatterns = patterns('cococloud.selection.views',
    url(r'^area/(?P<area_id>\d+)/$', 'get_products', name='selection_products'),
    url(r'^customization_options/(?P<product_id>\d+)/$', 'customization_options', 
        name='selection_customization_options'),
    url(r'^customize/(?P<product_id>\d+)/$', 'customize_product', 
        name='selection_customize'),
)
