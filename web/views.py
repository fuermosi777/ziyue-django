from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *
from api import encrypter

def home(request):
    category_instance = Category.objects.get(slug='technews')
    posts = Post.objects.filter(vendor__is_alive=True, vendor__categorys__in=[category_instance]).order_by('-datetime')[:50]
    categorys = Category.objects.all()
    for p in posts:
        p.encoded_id = encrypter.encode(p.id)
    context = {
        'posts': posts,
        'categorys': categorys,
    }
    return render(request, 'home.html', context)

def category(request, category_slug):
    category_instance = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(vendor__is_alive=True, vendor__categorys__in=[category_instance]).order_by('-datetime')[:50]
    categorys = Category.objects.all()
    for p in posts:
        p.encoded_id = encrypter.encode(p.id)
    context = {
        'posts': posts,
        'category': category_instance,
        'categorys': categorys,
    }
    return render(request, 'category.html', context)

def post(request, post_id):
    try:
        post_id = encrypter.decode(post_id)
    except:
        return HttpResponse(status=404)
    try:
        post_instance = Post.objects.get(id=post_id)
    except:
        post_instance = None
        return HttpResponseRedirect('/')
    context = {
        'post': post_instance
    }
    return render(request, 'post.html', context)

def vendor(request, vendor_id):
    try:
        vendor_id = encrypter.decode(vendor_id)
    except:
        return HttpResponse(status=404)
    vendor_instance = Vendor.objects.get(id=vendor_id)
    posts = Post.objects.filter(vendor=vendor_instance).order_by('-datetime')[:30]
    for p in posts:
        p.encoded_id = encrypter.encode(p.id)  
    context = {
        'vendor': vendor_instance,
        'posts': posts,
    }
    return render(request, 'vendor.html', context)