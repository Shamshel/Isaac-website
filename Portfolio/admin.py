from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_date', 'published')

	fieldsets = [
		(None, {'fields':['author', 'title', 'link', 'abstract', 'text', 'image']}),
		('Publishing Information', {'fields':['created_date', 'published', 'published_date', 'modified_date']}),
	]
	list_filter = ['created_date', 'published']
	search_fields = ['title', 'abstract', 'text']

admin.site.register(Project, ProjectAdmin)

