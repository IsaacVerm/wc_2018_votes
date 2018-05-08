from django.urls import path
from . import views

urlpatterns = [
    path('', views.options, name = 'options'),
    path('about/', views.about, name = 'about')
]
