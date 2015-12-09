from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Post

def post_list(request):
	posts = Post.objects.filter(published=True).order_by('-published_date')[:5]
	return render(request, 'Blogs/index.html', { 'posts':posts })

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)

	if post.published is False:
		raise Http404("Post is not yet published or does not exist.")

	return render(request, 'Blogs/post_detail.html', { 'post':post })
