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
	text = models.TextField(help_text="Text can contain HTML tags (and scripts, be careful).")
	link = models.CharField(max_length=200, blank=True, null=True)
	thumbnail = models.ImageField(upload_to=get_image_path, blank=True, null=True, help_text="Thumbnail should be 700x300 (7:3). Thumbnail will be used in portfolio listing. If blank, the image will be used.")
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True, help_text="Image should be 750x300 (15:10). Image will be used in portfolio detail.")

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

