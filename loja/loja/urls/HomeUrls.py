from django.urls import path #type: ignore
from loja.views.HomeView import home_view
urlpatterns = [
    path("", home_view, name= 'home'),
]