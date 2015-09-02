import sys
from django.core.management.base import BaseCommand, CommandError
from api.models import *
from datetime import datetime, timedelta
from processor import storer
from multiprocessing import Pool
from django.db import connection

def update_vendor_post(vendor):
    counter = 0
    success = False
    connection.close()
    spider = getattr(__import__('processor.spider', fromlist=[str(vendor.slug)]), str(vendor.slug))
    try:
        post_list = spider.crawl()
        success = True
    except:
        success = False
    if post_list:
        for p in post_list:
            stored = storer.store(vendor, p)
            if stored:
                counter = counter + 1
    log = Update_log(success=success, counter=counter, vendor=vendor)
    log.save()

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