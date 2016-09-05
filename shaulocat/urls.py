from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shaulocat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^yo/$', 'app.views.yo', name='callback')
)
