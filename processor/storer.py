from api.models import *
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib2

def store(vendor, post):
    try:
        p = Post.objects.get(title=post['title'])
        print 'Post already exists %s'%post['title']
    except:
        p = Post(title=post['title'], vendor=vendor, body=post['body'], source=post['source'], datetime=post['datetime'])
        p.save()
        if 'feature' in post:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(post['feature']).read())
            img_temp.flush()

            p.feature = File(img_temp)
            p.save()

        print 'New post added %s'%p.title