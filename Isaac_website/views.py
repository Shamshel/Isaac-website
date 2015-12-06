from django.shortcuts import render

from Blogs.models import Post

def index(request):
	return render(request, 'Isaac_website/index.html', { })

