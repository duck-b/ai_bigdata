from rest_framework import serializers
from .models import MMovie, MAge, MCast, MComment, MGender, MPoint

# from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
# from matplotlib import pyplot as plt
import pandas as pd
import operator
# import numpy as np

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'cast_id',
            'cast_actor',
            'cast_cast'
        )
        model = MCast

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'age_view10',
            'age_view20',
            'age_view30',
            'age_view40',
            'age_view50',
            'age_sati10',
            'age_sati20',
            'age_sati30',
            'age_sati40',
            'age_sati50'
        )
        model = MAge

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'comment_id',
            'comment_userid',
            'comment_username',
            'comment_point',
            'comment_contents'
        )
        model = MComment

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'gender_man',
        )
        model = MGender

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'point_dir',
            'point_act',
            'point_sto',
            'point_vis',
            'point_ost'
        )
        model = MPoint

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'movie_id',
            'movie_title',
            'movie_url',
            'movie_aud',
            'movie_net',
            'movie_rep',
            'movie_poster',
            'movie_genre',
            'movie_country',
            'movie_runtime',
            'movie_release',
            'movie_director',
            'movie_age',
            'movie_content',
        )
        model = MMovie
    
    
class MovieSerializer(serializers.ModelSerializer):
    cast = CastSerializer(many=True, read_only=True)
    age = AgeSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    gender = GenderSerializer(many=True, read_only=True)
    point = PointSerializer(many=True, read_only=True)
    keyword = serializers.SerializerMethodField(method_name='get_keyword')
    class Meta:
        fields = (
            'movie_id',
            'movie_title',
            'movie_url',
            'movie_aud',
            'movie_net',
            'movie_rep',
            'movie_poster',
            'movie_genre',
            'movie_country',
            'movie_runtime',
            'movie_release',
            'movie_director',
            'movie_age',
            'movie_content',
            'cast',
            'age',
            'comment',
            'gender',
            'point',
            'keyword'
        )
        model = MMovie
         
    def get_keyword(self, obj):
        comments = MComment.objects.filter(movie_id = obj.movie_id)
        
        del_word = ['영화','정말','우리','진짜','지금','대해','보고','놀란','한번']

        # df = pd.read_csv('./wordcloud.csv',encoding='cp949')

        # df = df[df['id'] == 24452] #여기에 영화 id를 넣어주세요.

        text = []
        for i in range(len(comments)):
            text.append(comments[i].comment_contents)
                
        # text = df['text'].tolist()

        text = [x for x in text if pd.isnull(x) == False]

        text = "".join(str(_)for _ in text)

        okt = Okt()
        nouns = okt.nouns(text) # 명사만 추출

        words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

        c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함  

        for key in list(c.keys()):
            if c[key] < 3:
                del c[key]  

        for word in del_word:
            if word in c.keys():
                del c[word]
                
        return c
    
class SearchSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        fields = (
            'movie_id',
            'movie_genre',
            'comment'
        )
        model = MMovie