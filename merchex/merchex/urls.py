"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello),
    path("about/", views.about),
    path("listings/", views.listings),
    path("bands/", views.band_list, name="bands"),
    path("contact/", views.contact),

    path("bands/<int:band_id>/", views.band_detail, name="band-detail"),
    path("bands/<int:band_id>/change", views.band_update, name="band-update"),
    path("bands/<int:band_id>/delete", views.band_delete, name="band-delete"),
    path("bands/add/", views.band_create, name="band_create")
]