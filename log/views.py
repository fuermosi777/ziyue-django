from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *
from datetime import datetime, timedelta

@login_required
@never_cache
def log(request):
    start = request.GET.get('start', None)
    if not start:
        return HttpResponse(status=404)
    else:
        start = int(start)
        dates = []
        now = datetime.now()
        for x in range(1, 10):
            dates.append(now - timedelta(days=x))
        vendors = Vendor.objects.all().prefetch_related('post_set')[start:start+50]

        for v in vendors:
            posts = list(v.post_set.all())
            v.data = [0] * 9
            for idx, val in enumerate(dates):
                v.data[idx] = {
                    'datetime': (val - datetime(1970,1,1)).total_seconds(),
                    'num': 0,
                }
                for p in posts:
                    if p.datetime.year == val.year and p.datetime.month == val.month and p.datetime.day == val.day:
                        v.data[idx]['num'] += 1

        context = {
            'vendors': vendors,
        }
        return render(request, 'log/log.html', context)