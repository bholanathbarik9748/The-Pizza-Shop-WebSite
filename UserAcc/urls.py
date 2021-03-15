from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import regester

urlpatterns = [
    path("regester/", views.regester, name="regester"),
]
