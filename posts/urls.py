from django.urls import path
from . import views
from django.views.generic import TemplateView

# CRUD -> listar, detalle, crear, eliminar, actualizar

urlpatterns = [
    path('', views.post_list, name="post_list"),

    path('post/new', views.PostCreate.as_view(), name="post_new"),

    path('vehiculo/new', views.VehiculoCreate.as_view(), name="vehiculo_new"),

    path('vehiculo/<int:pk>/delete/', views.VehiculoDelete.as_view(), name="vehiculo-delete"),

    path('info/', views.Info.as_view(), name="info"),
    ]
