from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'inzain.blog.views.index', name='blog-index'),
    url(r"^archive/$", 'inzain.blog.views.archive', name="blog-archive"),
    url(r"^feeds/$", 'django.views.generic.simple.direct_to_template', 
        dict(template='feeds.html'), name="blog-feeds"),
    url(r"^(?P<slug>[-\w]+)/", 'inzain.blog.views.blogpost', name="blog-post"),
)