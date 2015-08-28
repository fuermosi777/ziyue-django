from django.db import models
import uuid, os

class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name

def author_avatar_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/author_avatar', filename)

class Vendor(models.Model):
	name = models.CharField(max_length=30)
    url = models.URLField()
    avatar = models.ImageField(upload_to=author_avatar_name)
    def __str__(self):
        return self.name

class Post(models.Model):
	title = models.TextField()

    def __str__(self):
        return self.title