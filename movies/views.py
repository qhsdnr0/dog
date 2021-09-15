from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .models import Actor, Movie, Actor_movie

# Create your views here.
class ActorView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        act = Actor.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"],
        )

        return JsonResponse({"MESSAGE" : "CREATED"}, status = 201)

    def get(self, request) :
        actor_list = []
        actors = Actor.objects.all()
        
        for act in actors :    
            actor_list.append(
                {
                    "first_name" : act.first_name,
                    "last_name" : act.last_name,
                    "movie" : [i.movie.title for i in Actor_movie.objects.filter(actor=act.id)],
                }
            )
            
        return JsonResponse({"result" : actor_list}, status = 200)

class MovieView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        Movie.objects.create(
            title = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"],
        )

        return JsonResponse({"MESSAGE" : "CREATED"}, status = 201)

    def get(self, request) :
        movie_list = []
        movies = Movie.objects.all()
        for movi in movies :
            movie_list.append(
                {
                    "title" : movi.title,
                    "running_time" : movi.running_time,
                    "release_date" : movi.release_date,
                    "actor" : [i.actor.first_name for i in Actor_movie.objects.filter(movie=movi.id)]
                }
            )
        return JsonResponse({"result" : movie_list}, status = 200)

class Actor_movieView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        Actor_movie.objects.create(
            actor = Actor.objects.get(pk=int(data["actor"])),
            movie = Movie.objects.get(pk=int(data["movie"]))
        )

        return JsonResponse({"MESSAGE" : "CREATED"}, status = 201)