from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', include('base.urls')),
    path('votes/', include('votes.urls')),
    path('hall_of_shame/', include('hall_of_shame.urls')),
    path('admin/', admin.site.urls)
]
