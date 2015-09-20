from django.contrib.sitemaps import Sitemap
from api.models import *

class WebSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.order_by('-datetime')[:500]