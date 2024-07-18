from django.urls import path
from .views import hello
from .views import client_infos, process_test_request

urlpatterns = [
    path('hello/', hello),
    path('commande-infos/<int:id>', client_infos),
    path('test-request/', process_test_request)
]