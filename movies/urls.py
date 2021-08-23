from django.urls import path

from .views import *
from .api import *


urlpatterns = [
    path("movie/", MovieListView.as_view()),
    path("movie/<int:pk>/", MovieDetailView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
    path('actors/', ActorListView.as_view()),

    path('actor/', ActorViewSet.as_view({'get': 'list'})),
    path('actor/<int:pk/>', ActorViewSet.as_view({'get': 'retrieve'})),

    path('actors/<int:pk>', ActorDetailView.as_view()),
    path("review/<int:pk>", ReviewDestroy.as_view()),
]
