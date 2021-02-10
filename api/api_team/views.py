from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from apps.team.models import Team, UserTeamAssignment, User
from api.api_team.serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            return self.queryset.filter(userteamassignment__user__id=user_id)
        return self.queryset


    @action(methods=['put'], detail=True)
    def add_member(self, request, pk=None, **kwargs):
        try:
            members = request.data['members']
            team = self.queryset.get(pk=pk)
            for member in members:
                user = User.objects.get(pk=member)
                UserTeamAssignment.objects.create(team=team, user=user)
            #send_push_notification("user_add_star", "New star assigned", user.id)
            return Response("Member added to Team {}".format(self.name, 200))
        except Exception as e:
            return Response(e.__str__)

    @action(methods=['put'], detail=True)
    def set_team_admin(self, request, pk=None, **kwargs):
        try:
            user_id = request.data['user_id']
            if User.objects.filter(pk=user_id).exists():
                print("CCCCCCCCCCCCCCC")
                user_team_ass = UserTeamAssignment.objects.get(team__pk=pk, user__pk=user_id) 
                user_team_ass.is_team_admin = True
                user_team_ass.save()             
            #send_push_notification("user_add_star", "New star assigned", user.id)
            return Response("User {} is now admin of Team {}".format(user_id, pk, 200))
        except Exception as e:
            return Response(e.__str__)
    #def get(self, request, *args, **kwargs):
    #    teams = Team.objects.all()
    #    serializer = TeamSerializer(teams, many=True)
    #    return Response(serializer.data, 200)
    #def post(self, request, *args, **kwargs):
