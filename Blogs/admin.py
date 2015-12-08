from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_date', 'published')

	fieldsets = [
		(None, {'fields':['author', 'title', 'abstract', 'text', 'image']}),
		('Publishing Information', {'fields':['created_date', 'published', 'published_date', 'modified_date']}),
	]
	list_filter = ['created_date', 'published']
	search_fields = ['title']

admin.site.register(Post, PostAdmin)
