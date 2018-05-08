from django.urls import path
from . import views

urlpatterns = [
    path('', views.options, name = 'options'),
    path('users/', views.users, name = 'users'),
    path('users/ranking/', views.ranking, name = 'ranking'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.make_prediction, name='make_prediction'),
    path('games/<int:game_id>/predictions', views.predictions, name='predictions'),
    path('games/<int:game_id>/confirm_prediction', views.confirm_prediction, name='confirm_prediction')
]