from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    score = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    times_cheated = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s-%s' % (self.home_team, self.away_team)