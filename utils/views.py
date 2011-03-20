"""
Generic snippet for class based views
"""

class View(object):
    def __new__(cls, request, **kwargs):
        obj = super(View, cls).__new__(cls)
        return obj(request, **kwargs)
    
    def __init__(self):
        pass
        
    def __call__(self, request, **kwargs):
        pass

class GetPostView(View):
    def __call__(self, request, **kwargs):
        if request.POST:
            return self.Post(request, **kwargs)
        return self.Get(request, **kwargs)
    
    def Get(self, request, **kwargs):
        pass
        
    def Post(self, request, **kwargs):
        pass
