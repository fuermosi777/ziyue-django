from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Vendor(models.Model):
	name = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.name

class Post(models.Model):
	title = models.TextField()

    def __str__(self):
        return self.title