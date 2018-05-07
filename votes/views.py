from django.shortcuts import render
from .models import Game, Prediction
from django.http import HttpResponseRedirect, HttpResponse # temp for placeholders

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    
    return render(request, 'votes/games.html', context)
    
def make_prediction(request, game_id):
    selected_game = Game.objects.get(pk=game_id)
    
    context = {'selected_game': selected_game}
    return render(request, 'votes/make_prediction.html', context)
    
def predictions(request, game_id):
    predictions = Prediction.objects.filter(game=Game.objects.get(pk=game_id))
    context = {'predictions': predictions}
    
    return render(request, 'votes/predictions.html', context)
    
def confirm_prediction(request, game_id):
    prediction = Prediction(game = Game.objects.get(pk=game_id), user = request.POST.get('user'), goals_home_team = request.POST.get('home_goals'), goals_away_team = request.POST.get('away_goals'))
    prediction.save()
    
    selected_game = Game.objects.get(pk=game_id)
    
    context = {'prediction': prediction, 'selected_game': selected_game}
    return render(request, 'votes/confirm_prediction.html', context)