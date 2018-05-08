from django.db import models
from hall_of_shame.models import User

class Game(models.Model):
    round = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(null=True)
    home_team = models.CharField(max_length=50, null=True)
    away_team = models.CharField(max_length=50, null=True)
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)
    finished = models.BooleanField(default=False)
    
    def is_finished(self):
        if isinstance(self.home_goals, int) and isinstance(self.away_goals, int):
            self.finished = True
    
    def __str__(self):
        return '%s-%s %s' % (self.home_team, self.away_team, self.date)
    
class Prediction(models.Model):
    # use date, home team and away team from Game (one-to-many)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    # use name from User (one-to-many)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    predicted_goals_home = models.IntegerField(default = 0)
    predicted_goals_away = models.IntegerField(default = 0)
    
    def __str__(self):
        return '%s-%s %s %s' % (self.game.home_team, self.game.away_team, self.game.date, self.user)
        
class Score(models.Model):
    # # use date, home_team, away_team, home_goals and away_goals from Game (one-to-many)
    # game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    # # use name from User (one-to-many)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    # use predicted_goals_home and predicted_goals_away from Prediction(one-to-one)
    prediction = models.OneToOneField(Prediction, on_delete=models.CASCADE, null=True)
    
    points = models.IntegerField(default = 0)
    
    def points_scored(self):
        home_goals_correct = self.prediction.predicted_goals_home == self.prediction.game.home_goals
        away_goals_correct = self.prediction.predicted_goals_away == self.prediction.game.away_goals
        
        if home_goals_correct and away_goals_correct:
            self.points = self.points + 1

    