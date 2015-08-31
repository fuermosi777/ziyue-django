import sys
from django.core.management.base import BaseCommand, CommandError
from api.models import *
from datetime import datetime, timedelta
from processor import storer
from multiprocessing import Pool
from django.db import connection

def update_vendor_post(vendor):
    print unicode(datetime.now())
    connection.close()
    spider = getattr(__import__('processor.spider', fromlist=[str(vendor.slug)]), str(vendor.slug))
    post_list = spider.crawl()
    for p in post_list:
        storer.store(vendor, p)

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        vendors = Vendor.objects.all()
        vendor_list = []
        for v in vendors:
            vendor_list.append(v)

        pool = Pool(10)
        pool.map(update_vendor_post, vendor_list)
        pool.close()
        pool.join()