from django.contrib import admin
from .models import Game, Prediction, Score, User

admin.site.register(Game)
admin.site.register(Prediction)
admin.site.register(Score)
admin.site.register(User)
