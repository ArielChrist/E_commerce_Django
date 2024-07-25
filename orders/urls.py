from django.urls import path
from .views import hello, client_infos, process_test_request, HomeView, index,get_client

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('commande-infos/<int:id>/', client_infos, name='client_infos'),
    path('test-request/', process_test_request, name='process_test_request'),
    path('cb-view/', HomeView.as_view()),
    path('home/', index, name='home'),
    path('catalog/<int:id>', get_client, name='get_client'),
]