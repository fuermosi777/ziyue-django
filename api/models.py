from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid, os

class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name

def vendor_avatar_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/vendor_avatar', filename)

class Vendor(models.Model):
	name = models.CharField(max_length=30)
    url = models.URLField()
    avatar = ProcessedImageField(upload_to=vendor_avatar_name, processors=[ResizeToFill(300, 300)], format='JPEG', options={'quality': 80})
    def __str__(self):
        return self.name

class Post(models.Model):
	title = models.TextField()

    def __str__(self):
        return self.title