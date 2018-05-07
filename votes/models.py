from django.db import models
from hall_of_shame.models import User

class Game(models.Model):
    round = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(null=True)
    home_team = models.CharField(max_length=50, null=True)
    away_team = models.CharField(max_length=50, null=True)
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)
    
    def __str__(self):
        return '%s-%s' % (self.home_team, self.away_team)
    
class Prediction(models.Model):
    # use date, home team and away team from Game (one-to-many)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    # use name from User (one-to-many)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    predicted_goals_home = models.IntegerField(default = 0)
    predicted_goals_away = models.IntegerField(default = 0)
    
    def __str__(self):
        return '%s-%s %s %s' % (self.game.home_team, self.game.away_team, self.game.date, self.user)
        
class Score(models.Model):
    # use date, home_team, away_team, home_goals and away_goals from Game (one-to-many)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    # use name from User (one-to-many)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # use predicted_goals_home and predicted_goals_away from Prediction(one-to-one)
    prediction = models.OneToOneField(Prediction, on_delete=models.CASCADE)
    
    score = models.IntegerField(default = 0)
    
    # def point_scored(self):
    #     # if predicted = actual => score +1

    