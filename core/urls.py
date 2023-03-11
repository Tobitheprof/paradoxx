from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.register, name="register"),
    path('register', views.register, name="register"),
    path('det', views.det, name="det"),
    path('profile', views.profile, name="profile")
    
]