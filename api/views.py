from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import *
from datetime import datetime, timedelta
import re
import itertools
from django.db.models import Q
from decorators import domain_verify

@domain_verify
def post(request):
    category = request.GET.get('category', None)
    start = request.GET.get('start', None)
    if not category or not start:
        return HttpResponse(status=500)
    else:
        start = int(start)
        category_instance = Category.objects.get(slug=category)
        posts = Post.objects.filter(vendor__categorys__in=[category_instance]).order_by('-id')[start:start+15]
        res = [{
            'id': p.id,
            'title': p.title,
        } for p in posts]
        return JsonResponse(res, safe=False)