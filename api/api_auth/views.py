from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from apps.team.models import User
from api.api_auth.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['put'], detail=True)
    def add_star(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.star_counter += 1
        user.save()
        return Response("Star added to user {}".format(user.__str__()), 200)

    @action(methods=['put'], detail=True)
    def remove_star(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.star_counter -= 1
        user.save()
        return Response("Star removed to user {}".format(user.__str__()), 200)