from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'inzain.blog.views.index', name='blog-index'),
    url(r"^archive/$", 'inzain.blog.views.archive', name="blog-archive"),
    url(r'^search/$', 'django.views.generic.simple.direct_to_template', 
        dict(template="comingsoon.html")),
    url(r"^(?P<slug>[-\w]+)/", 'inzain.blog.views.blogpost', name="blog-post"),
)