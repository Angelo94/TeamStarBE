from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
from apps.team.models import User, UserTeamAssignment
from api.api_auth.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.team.utils import send_push_notification

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
    def add_star(self, request, pk=None, **kwargs):
        team_id = request.query_params.get('team', None)
        if team_id is not None:
            uta = UserTeamAssignment.objects.filter(team_id=team_id, user_id=pk)
            if len(uta) == 1:
                uta[0].star_counter += 1
                uta[0].save()
                send_push_notification("user_add_star", "New star assigned", uta[0].user.id)
                return Response("Star added to user {}".format(uta[0].user.__str__()), 200)
            else:
                return Response(data="Duplicated <uta>", status=status.HTTP_400_BAD_REQUEST)

        return Response(data="Error on retrieve user or team", status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def remove_star(self, request, pk=None, **kwargs):
        team_id = request.query_params.get('team', None)
        if team_id is not None:
            uta = UserTeamAssignment.objects.filter(team_id=team_id, user_id=pk)
            if len(uta) == 1:
                uta[0].star_counter -= 1
                uta[0].save()
                send_push_notification("user_add_star", "New star assigned", uta[0].user.id)
                return Response("Star added to user {}".format(uta[0].user.__str__()), 200)
            else:
                return Response(data="Duplicated <uta>", status=status.HTTP_400_BAD_REQUEST)

        return Response(data="Error on retrieve user or team", status=status.HTTP_400_BAD_REQUEST)