from api.models import *
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib2
from bs4 import BeautifulSoup as BS
import pytz
from datetime import timedelta, datetime
from random import randint
from urlparse import urlparse, urljoin
import uuid, os
import mimetypes

def store(vendor, post):
    p = Post(title=post['title'], vendor=vendor, body=post['body'], source=post['source'], datetime=random_date())
    try:
        p.save()
        body = extract_images(vendor, p)
        p.body = body
        p.save()
        print 'New post added %s'%p.title
    except:
        print 'Post already exists %s'%post['title']
        pass

def random_date():
    return datetime.now(pytz.utc) + timedelta(minutes=randint(-20, 0))

def url_add_pre(pre, url):
    # turn url such as '/xxx.jpg' to 'http://aa.com/xxx.jpg'
    parse_res = urlparse(url)
    if not parse_res.netloc:
        return urljoin(pre, url)
    else:
        return url

def extract_images(vendor, post):
    soup = BS(post.body)
    for img in soup.findAll('img'):
        img_src = url_add_pre(vendor.url, img['src'])
        img['src'] = img_src
        img['src'] = store_post_image_from_url(vendor, img_src, post)
    return unicode(soup)

def store_post_image_from_url(vendor, image_url, post):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        # 'Accept-Encoding': 'none',
        # 'Accept-Language': 'en-US,en;q=0.8',
        # 'Connection': 'keep-alive',
        'referer': vendor.url,
    }
    if urlparse(image_url).scheme == 'data':
        print image_url
        return image_url
    else:
        ext = mimetypes.guess_extension(mimetypes.guess_type(image_url)[0])
        request = urllib2.Request(image_url, headers=headers)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urllib2.urlopen(request).read())
        img_temp.flush()

        p = Post_image(post=post)
        p.image.save('%s%s'%(uuid.uuid4(), ext), File(img_temp))
        p.save()
        print p.image.url
        return p.image.url

def filter_list(list):
    # remove existing article's titles
    res = []
    for l in list:
        try:
            p = Post.objects.get(source=l)
            print 'Post exists before trying to get full: %s, stop'%l
        except:
            res.append(l)
    return res