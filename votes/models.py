from django.db import models

class Game(models.Model):
    round = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(null=True)
    home_team = models.CharField(max_length=50, null=True)
    away_team = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return '%s-%s' % (self.home_team, self.away_team)
    
class Prediction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=50, null=True)
    goals_home_team = models.IntegerField(null=True)
    goals_away_team = models.IntegerField(null=True)
    
    def __str__(self):
        return '%s %s' % (self.game, self.user)
    
    