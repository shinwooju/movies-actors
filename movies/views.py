import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie

class ActorsView(View):
    def post(self, request):
        data        = json.loads(request.boby)
        
        actor       = Actor.objects.create(
            first_name      = data['first_name'],
            last_name       = data['last_name'],
            date_of_birth   = data['date_of_birth'],
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        actors   = Actor.objects.all()
        results  = []
        for actor in actors:
                results.append(
                    {
                    "first_name"    : actor.first_name,
                    "last_name"     : actor.last_name,
                    "date_of_birth" : actor.date_of_birth,
                    }
                )
        return JsonResponse({'results':results}, status=200)


class MoviesView(View):
    def post(self, request):
        data        = json.loads(request,body)

        movie       = Movie.objects.create(
            
            title           = data['title'],
            release_data    = data['release_data'],
            running_time    = data['running_time'],
            )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        actors  = Movie.objects.all()
        results  = []
        for movie in actors:
            results.append(
                {
                    "title"         : movie.title,
                    "release_data"  : movie.release_date,
                    "running_time"  : movie.running_time,
                }
            )
        return JsonResponse({'results':results}, status=200)