from django.urls import path
from . import views

app_name = "loja"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("restrita/", views.area_restrita, name="area_restrita"),
]
