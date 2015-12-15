from django.db import models
from django.utils import timezone

import os

def get_image_path(instance, filename):
	return os.path.join('project_media', str(instance.id), filename)

class Project(models.Model):
	# Project data
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=200, blank=True, null=True)
	text = models.TextField()
	link = models.CharField(max_length=200, blank=True, null=True)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

	# Project metadata
	created_date = models.DateTimeField(default=timezone.now)
	published = models.BooleanField(default=False)
	published_date = models.DateTimeField(blank=True, null=True)
	modified_date = models.DateTimeField(blank=True, null=True)
	
	# TODO:
	#	auto cached readme from git
	#	auto cached latest commit text
	

	def publish(self):
		self.published = True
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

