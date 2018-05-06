from django.http import HttpResponse
from .models import Game
import datetime

def overview(request):
    games = Game.objects.all()
    output = ', '.join([game.date.strftime("%Y-%m-%d %H:%M") for game in games])
    
    return HttpResponse(output)