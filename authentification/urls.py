from django.urls import path
from .views import signin_view, signup_view, logout_view

urlpatterns = [
    path('authentification/signup/', signup_view,name='signup'),
    path('authentification/signin/', signin_view,name='signin'),
    path('authentification/logout/', logout_view,name='logout'),
]