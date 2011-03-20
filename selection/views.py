from cococloud.utils.json import JsonResponse

from cococloud.selection.models import Product

def get_products(request, area_id):
    options = list(Product.objects.filter(area=area_id).values('name', 'price'))
    return JsonResponse({'status':'success', 'message': None,
                         'payload':options})

def customization_options(request, product_id):
    """
    Returns a description of the forms that need to be shown for
    customization
    """
    items = [{'xtype':'select', 'name':'reminder', 'label':'reminder', 
              'options': [{'text':'10min', 'value':'10min',},
                          {'text':'30min', 'value':'30min',}] }]

    return JsonResponse({'status':'success', 'message': None,
                         'payload':items})


def customize_product(request, product_id):
    """
    Stores a customization option for the product/user in cache, so
    that it is available for the later stages
    """
    return JsonResponse({'status':'success', 'message': None,
                         'payload':[]})
    
