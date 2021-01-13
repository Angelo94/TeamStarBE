from apps.team.models import Team
from rest_framework import serializers
from api.api_auth.serializers import UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = "__all__"