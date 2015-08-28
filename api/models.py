from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid, os
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name

def vendor_avatar_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/vendor_avatar', filename)

@python_2_unicode_compatible
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    url = models.URLField()
    avatar = ProcessedImageField(upload_to=vendor_avatar_name, processors=[ResizeToFill(300, 300)], format='JPEG', options={'quality': 80})
    categorys = models.ManyToManyField(Category)
    def __str__(self):
        return self.name

def post_feature_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/post_feature', filename)

@python_2_unicode_compatible
class Post(models.Model):
    title = models.TextField()
    feature = ProcessedImageField(upload_to=vendor_avatar_name, processors=[ResizeToFill(800, 600)], format='JPEG', options={'quality': 80}, blank=True)
    vendor = models.ForeignKey(Vendor)
    datetime = models.DateTimeField(auto_now=True)
    body = models.TextField()
    source = models.URLField()

    def __str__(self):
        return self.title