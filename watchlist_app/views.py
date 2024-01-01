# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
# from watchlist_app.models import Movie

# # Create your views here.


# class MovieListView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         data = {"movies": list(movies.values())}
#         return JsonResponse(data)


# class MovieDetailView(View):
#     def get(self, request, id):
#         movie = Movie.objects.get(pk=id)
#         data = {
#             "name": movie.name,
#             "description": movie.description,
#             "active": movie.active,
#         }
#         return JsonResponse({"movie": data})
