from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('ranking/', views.ranking, name = 'ranking'),
    path('ranking/profile/<int:user_name>/', views.profile, name = 'profile'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.make_prediction, name='make_prediction'),
    path('games/predictions/<int:game_id>', views.predictions, name='predictions'),
    path('games/results/<int:game_id>', views.results, name='results'),
    path('games/confirm_prediction/<int:game_id>', views.confirm_prediction, name='confirm_prediction')
]