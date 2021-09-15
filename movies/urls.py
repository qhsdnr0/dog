from django.urls import path
from .views import Actor_movieView, MovieView, ActorView

urlpatterns = [
    path('/actors', ActorView.as_view()),
    path('/movies', MovieView.as_view()),
    path('/actors_movies', Actor_movieView.as_view()),
]
