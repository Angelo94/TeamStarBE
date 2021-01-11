from django.db import models

class Team(models.Model):
    team_name = models.CharField("team name", max_length=100)
    
    def __str__(self):
        return self.team_name