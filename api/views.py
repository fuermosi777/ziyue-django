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
            posts = Post.objects.filter(vendor__is_alive=True).filter(vendor__categorys__in=[category_instance])
        if vendor_id:
            posts = Post.objects.filter(vendor__is_alive=True).filter(vendor_id=vendor_id)
        posts = posts.order_by('-datetime')[start:start+15]
        res = {
            'data': [{
                'id': encrypter.encode(p.id),
                'title': p.title,
                'datetime': tools.humanize_timesince(p.datetime),
                'source': p.source,
                'vendor': {
                    'name': p.vendor.name,
                    'avatar': p.vendor.avatar.url,
                    'url': p.vendor.url,
                },
            } for p in posts],
            'hasNext': True,
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
                'title': post_instance.title,
                'body': post_instance.body,
                'datetime': tools.humanize_timesince(post_instance.datetime),
                'source': post_instance.source,
                'vendor': {
                    'name': post_instance.vendor.name,
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
        posts = Post.objects.filter(title__icontains=q).order_by('-datetime')[start:start+30]
        if posts:
            res = {
                'data':[{
                    'id': encrypter.encode(p.id),
                    'title': p.title,
                    'datetime': tools.humanize_timesince(p.datetime),
                    'source': p.source,
                    'vendor': {
                        'name': p.vendor.name,
                        'avatar': p.vendor.avatar.url,
                        'url': p.vendor.url,
                    },
                } for p in posts],
                'hasNext': False,
            }
            return JsonResponse(res, safe=False)
        else:
            return HttpResponse(status=404)
