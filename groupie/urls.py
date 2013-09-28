import re

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


def static(prefix, **kwargs):
    return patterns('',
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')),
            'django.views.static.serve', kwargs=kwargs),
    )

filepatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = filepatterns + patterns('',
    url(r'^$', 'groupie.app.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)