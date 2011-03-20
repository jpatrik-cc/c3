from django.contrib.gis.geos import Point

from cococloud.utils.json import JsonResponse
from cococloud.discovery.models import PaymentArea

def local_options(request):
    lat, long = request.GET.get('position', '13.18686,55.70605').split(',')
    p = Point(float(lat.strip()), float(long.strip()))
    options = PaymentArea.objects.filter(area__contains=p)
    payload = [{'id':i.id, 'identifier':i.identifier, 'owner':i.owner.name} 
               for i in options]
    return JsonResponse({'status':'success', 'message': None,
                         'payload':payload})
