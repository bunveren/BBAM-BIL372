"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users_list, name='users_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),

    path('user-follow/', views.user_follow_list, name='user_follow_list'),
    path('user-follow/<int:pk>/', views.user_follow_detail, name='user_follow_detail'),

    path('artists/', views.artists_list, name='artists_list'),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),

    path('tracks/', views.tracks_list, name='tracks_list'),
    path('tracks/<int:pk>/', views.track_detail, name='track_detail'),
]
