from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'^$', views.article, name='article'),
    url(r'^articleCreate/$', views.articleCreate, name='articleCreate'),
    url(r'^articleRead/(?P<articleId>[0-9]+)/$', views.articleRead, name='articleRead'),

]