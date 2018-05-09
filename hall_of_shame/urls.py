from django.urls import path
from . import views

urlpatterns = [
    path('', views.debtors, name='debtors')
]