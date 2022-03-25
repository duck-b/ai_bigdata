from urllib import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import MMovie, MAge, MCast, MComment, MGender, MPoint, Mitem
from .serializers import MovieSerializer, MovieListSerializer, SearchSerializer

from django.http import Http404
from django.http import HttpResponse

import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
from collections import Counter
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q

class Movie:
    def __init__(self,genre,*args):
        
        self._genre = genre #유저가 선택한 영화장르입니다.
        self._user_movie = args[0]   #유저가 선택한 영화제목입니다.
        self._course_similarity_df = None   # 상관관계 데이터프레임 변수

        
    def start(self):
        
        self.data_process()   
        
        return self.result_movie()
        
    def data_load(self):
        qs = Mitem.objects.filter(movie_genre = self._genre)
        q = qs.values('movie', 'user_id', 'comment_point')
        data = pd.DataFrame.from_records(q)
        return data
        
    def data_process(self):
        
        #데이터 프레임 피봇테이블로 변경
        user_score = self.data_load().pivot_table(index=['user_id'],columns=['movie'],values='comment_point')
        # nan값 처리 후 corr 상관분석
        user_scores = user_score.fillna(0)
        user_scores = user_scores.replace(np.nan,0)
        self._course_similarity_df = user_scores.corr(method='pearson')
                
    def get_similar_courses(self,course_name):

        similar_score = self._course_similarity_df[course_name]
        similar_score = similar_score.sort_values(ascending=False)
        return similar_score

    def result_movie(self):

        similar_scores = pd.DataFrame()
        
        for course in self._user_movie:
            similar_scores = similar_scores.append(self.get_similar_courses(course),ignore_index=True)
            
        result = similar_scores.sum().sort_values(ascending=False).head(13)

        result = list(result.index)
        result = result[3:]
        
        return result
    

class ListMovie(generics.ListCreateAPIView):
    queryset = MMovie.objects.all()
    serializer_class = MovieListSerializer

class SearchMovie(generics.ListCreateAPIView):
    queryset = MMovie.objects.all()
    serializer_class = MovieListSerializer

    def get_queryset(self, *args):
        q = []
        for i in range(len(args[0])):
            q.append(Q(movie_id = args[0][i]))
        try:
            return MMovie.objects.filter(q[0] | q[1] | q[2] | q[3] | q[4] | q[5] | q[6] | q[7] | q[8] | q[9])
        except MMovie.DoesNotExist:
            raise Http404
    
    def get(self, request, movie_genre, movie_id1, movie_id2, movie_id3):
        
        # 추천 시스템 들어감
            
        # movie_id1 = request.POST.get('movie_id1')
        # movie_id2 = request.POST.get('movie_id2')
        # movie_id3 = request.POST.get('movie_id3')
        # movie_genre = request.POST.get('movie_genre')
        
        movie_recommend = Movie(movie_genre,[int(movie_id1),int(movie_id2),int(movie_id3)])
        movie_list = movie_recommend.start()
        # print(movie_list)

        queryset = self.get_queryset(movie_list)
        serializer = MovieListSerializer(queryset, many=True)
        return Response(serializer.data)
    # def post(self, request):
        
    #     # 추천 시스템 들어감
            
    #     movie_id1 = request.POST.get('movie_id1')
    #     movie_id2 = request.POST.get('movie_id2')
    #     movie_id3 = request.POST.get('movie_id3')
    #     movie_genre = request.POST.get('movie_genre')
        
    #     movie_recommend = Movie(movie_genre,[int(movie_id1),int(movie_id2),int(movie_id3)])
    #     movie_list = movie_recommend.start()
    #     # print(movie_list)

    #     queryset = self.get_queryset(movie_list)
    #     serializer = MovieListSerializer(queryset, many=True)
    #     return Response(serializer.data)

class DetailMovie(generics.ListCreateAPIView):
    queryset = MMovie.objects.all()
    serializer_class = MovieSerializer
    
    def get_queryset(self, pk):
        try:
            return MMovie.objects.get(movie_id = pk)
        except MMovie.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)














# class DetailAge(generics.ListCreateAPIView):
#     queryset = MAge.objects.all()
#     serializer_class = AgeSerializer
    
#     def get_queryset(self, pk):
#         try:
#             return MAge.objects.get(movie = pk)
#         except MAge.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         queryset = self.get_queryset(pk)
#         serializer = AgeSerializer(queryset)
#         return Response(serializer.data)
    
# class DetailCast(generics.ListCreateAPIView):
#     queryset = MCast.objects.all()
#     serializer_class = CastSerializer
    
#     def get_queryset(self, pk):
#         try:
#             return MCast.objects.filter(movie = pk)
#         except MCast.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         queryset = self.get_queryset(pk)
#         serializer = CastSerializer(queryset)
#         return Response(serializer.data)