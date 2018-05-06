from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name='games'),
    path('<int:game_id>/', views.make_prediction, name='make_prediction'),
    path('<int:game_id>/predictions', views.predictions, name='predictions'),
    path('<int:game_id>/confirm_prediction', views.confirm_prediction, name='confirm_prediction')
]