from django.conf.urls.defaults import *
from django.shortcuts import redirect
from inzain.blog.feeds import LatestPosts

urlpatterns = patterns('',
    url(r'^$', 'inzain.blog.views.index', name='blog-index'),
    url(r"^archive/$", 'inzain.blog.views.archive', name="blog-archive"),
    url(r"^feed/$", lambda r: redirect('/blog/feeds/latest/')),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
            {'feed_dict': {'latest': LatestPosts}}),
    url(r'^search/$', 'django.views.generic.simple.direct_to_template', 
        dict(template="comingsoon.html")),
    url(r"^(?P<slug>[-\w]+)/", 'inzain.blog.views.blogpost', name="blog-post"),
)