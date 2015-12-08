from django.db import models
from django.utils import timezone

import os

def get_image_path(instance, filename):
	return os.path.join(str(instance.id), filename)

class Post(models.Model):
	# Post data
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=200, blank=True, null=True)
	text = models.TextField()
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

	# Post metadata
	created_date = models.DateTimeField(default=timezone.now)
	published = models.BooleanField(default=False)
	published_date = models.DateTimeField(blank=True, null=True)
	modified_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published = True
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
