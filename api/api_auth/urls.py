from django.urls import path, include
from rest_auth.views import LoginView
from api.api_auth import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
