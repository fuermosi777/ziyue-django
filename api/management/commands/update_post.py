import sys
from django.core.management.base import BaseCommand, CommandError
from api.models import *
from datetime import datetime, timedelta
from processor import storer
from multiprocessing import Pool
from django.db import connection

def update_vendor_post(vendor):
    spider = getattr(__import__('processor.spider', fromlist=[str(vendor.slug)]), str(vendor.slug))
    post_list = spider.crawl()
    for p in post_list:
        storer.store(vendor, p)
    connection.close()

class Command(BaseCommand):
    help = ""
    args = '<test>'
    def handle(self, *args, **options):
        vendors = Vendor.objects.filter(is_alive=True)
        if args:
            if args[0] == 'test':
                for v in vendors:
                    print '[TEST] start %s'%v.name
                    update_vendor_post(v)
            else:
                vendor = Vendor.objects.get(slug=args[0])
                print '[TEST] start %s'%vendor.name
                update_vendor_post(vendor)
        else:
            vendor_list = []
            for v in vendors:
                vendor_list.append(v)

            pool = Pool(10)
            pool.map(update_vendor_post, vendor_list)
            pool.close()
            pool.join()