from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Vendor(models.Model):
	name = models.CharField(max_length=30)

class Post(models.Model):
	title = models.TextField()