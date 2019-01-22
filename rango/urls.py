from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r"^v2$",views.v2,name="v2"),
	url(r"^$",views.index,name="index"),
]
