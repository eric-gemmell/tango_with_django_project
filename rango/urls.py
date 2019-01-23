from django.contrib import admin
from rango import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
	url(r"^$",views.index,name="index"),
	url(r"^about/",views.about,name="about"),
	url(r"admin/",admin.site.urls),
]
