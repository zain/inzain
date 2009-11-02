from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', dict(template="about.html")),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('inzain.blog.urls')),
    (r'^links/$', 'django.views.generic.simple.direct_to_template', 
        dict(template="comingsoon.html")),
    (r'^projects/$', 'django.views.generic.simple.direct_to_template', 
        dict(template="comingsoon.html")),
    (r"^feeds/$", 'django.views.generic.simple.direct_to_template', 
        dict(template='feeds.html')),
)

if settings.LOCAL_DEV:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )