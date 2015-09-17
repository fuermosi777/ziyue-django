"""ziyue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import api.views
import web.views
import log.views
import font.views

urlpatterns = [
    url(r'^gever/admin/', include(admin.site.urls)),
    url(r'^api/posts/$', api.views.posts),
    url(r'^api/posts/recommend/$', api.views.posts_recommand),
    url(r'^api/post/$', api.views.post),
    url(r'^api/post/search/$', api.views.post_search),
    url(r'^api/vendors/$', api.views.vendors),
    url(r'^api/vendor/posts/$', api.views.vendor_posts),
]

urlpatterns += [
    url(r'^$', web.views.home),
    url(r'^(?P<category_slug>\w+)$', web.views.category),
    url(r'^post/(?P<post_id>\w+)$', web.views.post),
    url(r'^vendor/(?P<vendor_id>\w+)$', web.views.vendor),
]

urlpatterns += [
    url(r'^log/log/$', log.views.log),
]

urlpatterns += [
    url(r'^font/main/$', font.views.main),
]