from django.urls import path
from django.conf.urls import include, handler404

from . import views

handler404 = 'blog.views.handler404'


urlpatterns = [
    path('', views.home,name='home'),
    path('nouveau_projet/', views.newProject,name='newProject'),
    path('post/(?P<id>[0-9]+)', views.show,name='show'),
]
