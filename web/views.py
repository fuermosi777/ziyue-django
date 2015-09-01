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
        'categorys': categorys,
    }
    return render(request, 'category.html', context)

def post(request, post_id):
    try:
        post_id = encrypter.decode(post_id)
    except:
        return HttpResponse(status=404)
    post_instance = Post.objects.get(id=post_id)
    context = {
        'post': post_instance
    }
    return render(request, 'post.html', context)

def vendor(request, vendor_id):
    context = {}
    return render(request, 'vendor.html', context)