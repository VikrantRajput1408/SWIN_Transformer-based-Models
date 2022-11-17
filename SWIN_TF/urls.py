"""SWIN_TF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from SWIN_TF import views
from django.conf import settings, urls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('models/', views.models),
    path('leaf/', views.leaf),
    path('forest/', views.forest),
    path('butterfly/', views.butterfly),
    path('flower/', views.flower),
    path('predictImage', views.predictImage, name='predictImage'),
    path('predictleaf', views.predictleaf, name='predictleaf'),
    path('predictforest', views.predictforest, name='predictforest'),
    path('predictbutterfly', views.predictbutterfly, name='predictbutterfly'),
    path('predictflower', views.predictflower, name='predictflower'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    