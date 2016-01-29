from django.db import models
from django.utils import timezone

import os

def get_image_path(instance, filename):
	return os.path.join('post_media', str(instance.id), filename)

class Post(models.Model):
	# Post data
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	abstract = models.CharField(max_length=500, blank=True, null=True)
	text = models.TextField(help_text="Text can contain HTML tags (and scripts, be careful).")
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True, help_text="Image should be 900x300 (3:1).")

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
