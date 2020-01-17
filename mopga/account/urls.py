from django.urls import path

from . import views

urlpatterns = [
    path('sign/', views.sign,name='signinup'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.deconnection,name='logout'),
    path('contacts/', views.contact,name='contact'),
    path('profile/', views.profile, name='profile'),
]
