"""movie_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import movie_list, actor_list, movie_detail, actor_detail, review_list
from .views import MovieList, MovieDetail, ActorList, ActorDetail, ReviewList

urlpatterns = [
    # path('movies', movie_list),
    path('movies', MovieList.as_view()),
    # path('movies/<int:pk>', movie_detail),
    path('movies/<int:pk>', MovieDetail.as_view()),

    # path('movies/<int:pk>/reviews', review_list),
    path('movies/<int:pk>/reviews', ReviewList.as_view()),

    # path('actors', actor_list),
    path('actors', ActorList.as_view()),
    # path('actors/<int:pk>', actor_detail),
    path('actors/<int:pk>', ActorDetail.as_view()),
]
