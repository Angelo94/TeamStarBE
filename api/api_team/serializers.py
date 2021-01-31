from apps.team.models import Team, UserTeamAssignment
from rest_framework import serializers
from api.api_auth.serializers import UserSerializer

class UserTeamAssignment(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserTeamAssignment
        exclude = ['id', 'team']

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    def get_members(self, obj):
        utas = obj.userteamassignment_set.all()
        serializer_data = UserTeamAssignment(utas, many=True).data
        return serializer_data
