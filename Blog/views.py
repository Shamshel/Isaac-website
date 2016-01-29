from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Post

def post_list(request, page=0):
	start = int(page)*5
	stop = start+5
	next_page = int(page)-1

	if stop < Post.objects.count():
		prev_page = int(page)+1

	else:
		prev_page = -1

	posts = Post.objects.filter(published=True).order_by('-published_date')[start:stop]
	return render(request, 'Blog/index.html', { 'posts':posts, 'page':page, 'next_page':next_page, 'prev_page':prev_page })

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)

	if post.published is False:
		raise Http404("Post is not yet published or does not exist.")

	return render(request, 'Blog/post_detail.html', { 'post':post })
