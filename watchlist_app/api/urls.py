from django.urls import path
from watchlist_app.api import views


urlpatterns = [
    path("list/", views.movie_list, name="list"),
    path("list/<int:id>", views.movie_detail, name="movie_detail"),
]
