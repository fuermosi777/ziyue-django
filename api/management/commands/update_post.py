import sys
from django.core.management.base import BaseCommand, CommandError
from api.models import *
from datetime import datetime, timedelta
from processor import storer

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        vendors = Vendor.objects.all()
        for v in vendors:
            spider = getattr(__import__('processor.spider', fromlist=[str(v.slug)]), str(v.slug))
            post_list = spider.crawl()
            for p in post_list:
                storer.store(v, p)