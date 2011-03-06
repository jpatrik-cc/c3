from cococloud.utils.json import JsonResponse

def point(request):
    return JsonResponse({'identifier':'test', 'owner':'test2'})
