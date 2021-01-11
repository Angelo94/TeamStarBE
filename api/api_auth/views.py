from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from api.api_auth.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer