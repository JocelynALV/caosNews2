from django.urls import path
from .views import home
from core.views import home

urlpatterns = [
    path('', home, name="home"),
]