from django.urls import path, include

urlpatterns = [
    path('votes', include('votes.urls'))
]
