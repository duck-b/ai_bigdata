from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListMovie.as_view()),
    path('recommend/<int:movie_genre>/<int:movie_id1>/<int:movie_id2>/<int:movie_id3>/', views.SearchMovie.as_view()),
    path('<int:pk>/', views.DetailMovie.as_view()),
]
