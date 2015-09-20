from django.contrib.sitemaps import Sitemap
from api.models import *
from api.encrypter import encode

class WebSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.order_by('-datetime')[:500]

    def get_absolute_url(self):
        return '/post/%s'%encode(self.id)