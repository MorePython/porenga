"""porenga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import api

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    path('api/v1/', api.urls),
    path('logout/', auth_views.logout, name='core_logout'),

    # enable the admin interface
    path('admin/', admin.site.urls),
]
