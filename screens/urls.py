from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'screens.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
                           name='logout'),
                       url(r'^screens/', include('website.urls', namespace='screens')),
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
