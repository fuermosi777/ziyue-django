from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *

@login_required
@never_cache
def log(request):
    vendors = Vendor.objects.all()
    for v in vendors:
        v.posts = Post.objects.filter(vendor=v).order_by('-datetime')[:20]
    context = {
        'vendors': vendors,
    }
    return render(request, 'log/log.html', context)