from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from inzain.blog.models import Post

def index(request):
    context = dict(posts=Post.objects.filter(completed=True)[0:5])
    return direct_to_template(request, 'blog/index.html', context)

def archive(request):
    context = dict(posts=Post.objects.filter(completed=True))
    return direct_to_template(request, 'blog/archive.html', context)

def blogpost(request, slug):
    post = get_object_or_404(Post, slug=slug, completed=True)
    return direct_to_template(request, 'blog/post.html', dict(post=post))