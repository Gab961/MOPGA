from django.urls import path

from . import views

urlpatterns = [
    path('sign/', views.sign,name='signinup'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
]
