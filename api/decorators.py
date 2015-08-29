from django.http import HttpResponse

def domain_verify(func=None):
    def _decorated(view_func):
        def _view(request, *args, **kwargs):
            if (request.META['HTTP_HOST'] not in ['ziyue.io', '127.0.0.1:8000', 'localhost:8000']):
                return HttpResponse(status=503)
            else:
                return view_func(request, *args, **kwargs)
        return _view
    if func is None:
        return _decorated
    else:
        return _decorated(func)