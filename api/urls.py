from .views import LoginAPI, ListUsers
from django.urls import path

urlpatterns = [

    path('users/', ListUsers.as_view()),
    path('login/', LoginAPI.as_view(), name='login'),
]