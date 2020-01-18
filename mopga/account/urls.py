from django.urls import path,re_path

from . import views

urlpatterns = [
    path('sign/', views.sign,name='signinup'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.deconnection,name='logout'),
    path('contacts/', views.contact,name='contact'),
    re_path('profile/(?P<username>[A-Za-z0-9]+)', views.profile, name='profile'),
]
