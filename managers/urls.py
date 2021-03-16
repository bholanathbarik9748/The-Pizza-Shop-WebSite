from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("payment/", views.payment, name="payment"),
    path("cp/", views.cp, name="cp"),
    path("OrderOnline/", views.OrderOnline, name="OrderOnline"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
