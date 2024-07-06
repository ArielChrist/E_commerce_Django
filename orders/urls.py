from django.urls import path
from .views import hello
from .views import client_infos

urlpatterns = [
    path('hello/', hello),
    path('commande-infos/<int:id>', client_infos)
]