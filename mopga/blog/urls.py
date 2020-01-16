from django.urls import include, path, re_path
from django.conf.urls import handler404

from . import views

handler404 = 'blog.views.handler404'


urlpatterns = [
    path('', views.home,name='home'),
    path('blog/', views.blog,name='blog'),
    path('archive/', views.archive,name='archive'),
    path('mentions/', views.mentions,name='mention'),
    path('nouveau_projet/', views.newProject,name='newProject'),
    re_path('projet/(?P<id>[0-9]+)', views.show,name='show'),
]
