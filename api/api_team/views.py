from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from apps.team.models import Team
from api.api_team.serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.
class TeamList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    #def get(self, request, *args, **kwargs):
    #    teams = Team.objects.all()
    #    serializer = TeamSerializer(teams, many=True)
    #    return Response(serializer.data, 200)
    #def post(self, request, *args, **kwargs):


class TeamDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Team.objects.all()
    serializer_class = TeamSerializer