from django.shortcuts import render
from rest_framework import generics

from .models import MMovie
from .serializers import MovieSerializer

class ListMovie(generics.ListCreateAPIView):
    queryset = MMovie.objects.all()
    serializer_class = MovieSerializer

class DetailMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = MMovie.objects.all()
    serializer_class = MovieSerializer