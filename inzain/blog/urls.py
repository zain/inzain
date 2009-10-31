from django.conf.urls.defaults import *

urlpatterns = patterns('inzain.blog.views',
    url(r'^$', 'index'),
)