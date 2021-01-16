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
from rest_framework.views import APIView


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id,'token': token.key})


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if User.objects.filter(username=request.data['username'], email=request.data['email']).exists():
                return Response('Username already exists', 400)
            else:
                user = User.objects.create(username=request.data['username'], password=request.data['password'], email=request.data['email'])
                user.save()
                return Response("User created", 200)
        except Exception as e:
            return Response(e.__str__())

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