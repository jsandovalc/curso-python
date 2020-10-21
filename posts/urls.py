from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name="post_list"),

    path('post/new', views.post_new, name="post_new"),

    path('vehiculo/new', views.vehiculo_new, name="vehiculo_new")
]
