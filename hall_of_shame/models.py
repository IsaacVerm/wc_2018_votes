from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    paid = models.BooleanField(default=False)
    times_cheated = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s' % (self.name)