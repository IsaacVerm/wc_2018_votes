from django.shortcuts import render
from .models import Game, Prediction, User, Score
from django.http import HttpResponse # temp for placeholders

def options(request):
    return render(request, 'votes/options.html')

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    
    return render(request, 'votes/games.html', context)
    
def users(request):
    return render(request, 'votes/users.html')
    
def ranking(request):
    # check which games are finished
    for game in Game.objects.all():
        game.is_finished()
        game.save()
    
    # get all predictions for finished games
    predictions = Prediction.objects.filter(game__finished = True)
    
    # flush out previous calculated scores (one-to-one relation between Prediction and Score)
    Score.objects.all().delete()
    
    # check if points are scored for each prediction
    for prediction in predictions:
        score = Score(prediction = prediction)
        score.points_scored()
        score.save()
        
    # setup dictionary for total points by users
    users = User.objects.all()
    
    total_points_by_user = {}
    for user in users:
        total_points_by_user[user.name] = 0
    
    # calculate total points by user
    for user in users:
        scores = Score.objects.filter(prediction__user__name = user.name)
        
        for score in scores:
            total_points_by_user[user.name] += score.points
            
    context = {'total_points_by_user': total_points_by_user}
    return render(request, 'votes/ranking.html', context)
    
def make_prediction(request, game_id):
    selected_game = Game.objects.get(pk=game_id)
    
    context = {'selected_game': selected_game}
    return render(request, 'votes/make_prediction.html', context)
    
def predictions(request, game_id):
    predictions = Prediction.objects.filter(game__id = game_id)
    
    if predictions.count() == 0:
        return render(request, 'votes/no_predictions_yet.html')
    
    context = {'predictions': predictions}
    return render(request, 'votes/predictions.html', context)
    
def confirm_prediction(request, game_id):
    name_submitted = request.POST.get('user')
    home_goals_submitted = request.POST.get('home_goals')
    away_goals_submitted = request.POST.get('away_goals')
    
    selected_game = Game.objects.get(pk=game_id)
    selected_user = User.objects.get(name = name_submitted)
    
    prediction = Prediction(game = selected_game,
                            user = selected_user,
                            predicted_goals_home = home_goals_submitted,
                            predicted_goals_away = away_goals_submitted)
    prediction.save()
    
    context = {'prediction': prediction}
    return render(request, 'votes/confirm_prediction.html', context)
    
