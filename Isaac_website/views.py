from django.shortcuts import render

from Blogs.models import Post

def index(request):
	posts = Post.objects.filter(published=True).order_by('-published_date')[:1]
	return render(request, 'Isaac_website/index.html', { 'posts':posts })

