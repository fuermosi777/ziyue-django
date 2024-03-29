# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import *
from datetime import datetime, timedelta
import re
import itertools
from django.db.models import Q
from decorators import domain_verify
import tools

import encrypter

@domain_verify
def posts(request):
    category = request.GET.get('category', None)
    vendor_id = request.GET.get('vendor_id', None)
    start = request.GET.get('start', None)
    if not (category or vendor_id) or not start or (category and vendor_id):
        return HttpResponse(status=500)
    else:
        start = int(start)
        if category:
            category_instance = Category.objects.get(slug=category)
            posts = Post.objects.filter(vendor__is_alive=True, vendor__categorys__in=[category_instance])
        if vendor_id:
            posts = Post.objects.filter(vendor__is_alive=True, vendor_id=vendor_id)
        posts = posts.order_by('-datetime')[start:start+30]
        res = {
            'data': tools.wrap_posts(posts),
            'hasNext': True,
        }
        return JsonResponse(res, safe=False)

@domain_verify
def posts_recommand(request):
    post_id = request.GET.get('post_id', None)
    if not post_id:
        return HttpResponse(status=500)
    else:
        post_id = encrypter.decode(post_id)
        post = Post.objects.get(id=post_id)
        posts = Post.objects.filter(vendor__is_alive=True, vendor__categorys__in=post.vendor.categorys.all()).order_by('?')[:5]
        res = {
            'data': tools.wrap_posts(posts),
            'hasNext': False,
        }
        return JsonResponse(res, safe=False)

@domain_verify
def post(request):
    post_id = request.GET.get('post_id', None)
    if not post_id:
        return HttpResponse(status=500)
    else:
        post_id = encrypter.decode(post_id)
        post_instance = Post.objects.get(id=post_id)
        if post_instance:
            res = {
                'id': encrypter.encode(post_instance.id),
                'title': post_instance.title,
                'body': post_instance.body,
                'datetime': tools.humanize_timesince(post_instance.datetime),
                'source': post_instance.source,
                'vendor': {
                    'name': post_instance.vendor.name,
                    'avatar': post_instance.vendor.avatar.url,
                    'url': post_instance.vendor.url,
                    'authorized': post_instance.vendor.authorizedBlog,
                },
            }
            return JsonResponse(res, safe=False)
        else:
            return HttpResponse(status=404)

@domain_verify
def post_search(request):
    q = request.GET.get('q', None)
    start = request.GET.get('start', None)
    if not q or not start:
        return HttpResponse(status=500)
    else:
        start = int(start)
        posts = Post.objects.filter(title__icontains=q).order_by('-datetime')[start:start+50]
        if posts:
            res = {
                'data': tools.wrap_posts(posts),
                'hasNext': False,
            }
            return JsonResponse(res, safe=False)
        else:
            return HttpResponse(status=404)

@domain_verify
def vendors(request):
    category = request.GET.get('category', None)
    if not category:
        return HttpResponse(status=500)
    else:
        vendors = Vendor.objects.filter(categorys__slug__in=[category])
        if vendors:
            res = [{
                'id': encrypter.encode(v.id),
                'name': v.name,
                'url': v.url,
                'avatar': v.avatar.url,
                'desc': v.desc,
                'authorized': v.authorizedBlog,
            } for v in vendors]
            return JsonResponse(res, safe=False)
        else:
            return HttpResponse(status=404)

@domain_verify
def vendor_posts(request):
    vendor_id = request.GET.get('vendor_id', None)
    start = request.GET.get('start', None)
    if not vendor_id or not start:
        return HttpResponse(status=500)
    else:
        vendor_id = encrypter.decode(vendor_id)
        start = int(start)
        vendor_instance = Vendor.objects.get(id=vendor_id)
        posts = Post.objects.filter(vendor__id=vendor_id).order_by('-datetime')[start:start+50]
        if posts:
            res = {
                'data': tools.wrap_posts(posts),
                'name': vendor_instance.name,
                'hasNext': False,
            }
            return JsonResponse(res, safe=False)
        else:
            return HttpResponse(status=404)