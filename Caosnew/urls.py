"""Caosnew URL Configuration

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
from django.urls import path, include
from core.views import NoticiaViewset, home, login, noticias, registro, horoscopo, periodista, NoticiaSerializer, noticias
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter() #nos permite crear urls necesarias para nuestra api
router.register('noticia', NoticiaViewset) #El viewset llama a todas las noticias  y aplica serializador  para pasarlas a Json


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('home', home, name='index'),
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
    path('horoscopo', horoscopo, name='horoscopo'),
    path('periodista', periodista, name='periodista'),
    path('api/', include(router.urls)),
    path('noticias/<id_noticia>',noticias, name='noticias'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
