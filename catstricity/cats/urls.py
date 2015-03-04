from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'cats.views.index'),
    url(r'^cat/(?P<id>\d+)$', 'cats.views.photo'),
)
