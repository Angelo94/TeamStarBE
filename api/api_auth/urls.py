from django.urls import path, include
from rest_auth.views import LoginView
from api.api_auth.views import UserViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

class UserView(DefaultRouter.APIRootView):
    pass

class MyDefaultRouter(DefaultRouter):
    root_view_name = 'users'
    APIRootView = UserView

router = MyDefaultRouter()

router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
