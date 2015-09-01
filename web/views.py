from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *
from api import encrypter

def home(request):
    return HttpResponseRedirect('/technews')

def category(request, category_slug):
    context = {}
    return render(request, 'category.html', context)

def post(request, post_id):
    try:
        post_id = encrypter.decode(post_id)
    except:
        return HttpResponse(status=404)
    context = {}
    return render(request, 'post.html', context)

def vendor(request, vendor_id):
    context = {}
    return render(request, 'vendor.html', context)