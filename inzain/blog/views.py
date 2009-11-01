from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from inzain.blog.models import Post

def index(request):
    return direct_to_template(request, 'index.html', dict(posts=Post.objects.all()[0:5]))

def archive(request):
    return direct_to_template(request, 'archive.html', dict(posts=Post.objects.all()))

def blogpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return direct_to_template(request, 'post.html', dict(post=post))