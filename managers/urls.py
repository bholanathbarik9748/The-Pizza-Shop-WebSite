from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("creteAcc/", views.creteAcc, name="creteAcc"),
    path("loginAcc/", views.loginAcc, name="loginAcc"),
    path("OrderOnline/", views.OrderOnline, name="OrderOnline"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
