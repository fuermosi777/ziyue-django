from api.models import *
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib2
from bs4 import BeautifulSoup as BS

def store(vendor, post):
    try:
        p = Post.objects.get(title=post['title'])
        print 'Post already exists %s'%post['title']
    except:

        p = Post(title=post['title'], vendor=vendor, body=post['body'], source=post['source'], datetime=post['datetime'])
        p.save()

        body = extract_images(vendor, p)
        p.body = body
        p.save()

        print 'New post added %s'%p.title

def extract_images(vendor, post):
    soup = BS(post.body)
    for img in soup.findAll('img'):
        print img['src']
        img['src'] = store_post_image_from_url(vendor, img['src'], post)
    return str(soup)

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

    request = urllib2.Request(image_url, headers=headers)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urllib2.urlopen(request).read())
    img_temp.flush()

    p = Post_image(image=File(img_temp), post=post)
    p.save()

    return p.image.url