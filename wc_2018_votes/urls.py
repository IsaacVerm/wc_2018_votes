from django.urls import path, include

urlpatterns = [
    path('votes/', include('votes.urls')),
    path('hall_of_shame/', include('hall_of_shame.urls'))
]
