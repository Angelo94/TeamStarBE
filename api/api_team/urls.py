from django.urls import path, include
from rest_auth.views import LoginView
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api.api_team.views import TeamViewSet
from rest_framework.routers import DefaultRouter

class TeamView(DefaultRouter.APIRootView):
    pass

class MyDefaultRouter(DefaultRouter):
    root_view_name = 'teams'
    APIRootView = TeamView

router = MyDefaultRouter()

router.register('team', TeamViewSet)


urlpatterns = [
    path('', include(router.urls))
]
