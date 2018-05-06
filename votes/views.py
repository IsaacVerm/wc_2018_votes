# from django.http import HttpResponse
# import datetime
from django.shortcuts import render
from .models import Game

def overview(request):
    games = Game.objects.all()
    context = {'games': games}
    
    return render(request, 'votes/overview.html', context)
    # output = ', '.join([game.date.strftime("%Y-%m-%d %H:%M") for game in games])
    # return HttpResponse(output)