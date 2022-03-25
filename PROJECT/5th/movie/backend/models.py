from urllib import response
from django.db import models
from django_db_views.db_view import DBView

# Create your models here.
class MAge(models.Model):
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='age', primary_key=True)
    age_view10 = models.IntegerField()
    age_view20 = models.IntegerField()
    age_view30 = models.IntegerField()
    age_view40 = models.IntegerField()
    age_view50 = models.IntegerField()
    age_sati10 = models.FloatField()
    age_sati20 = models.FloatField()
    age_sati30 = models.FloatField()
    age_sati40 = models.FloatField()
    age_sati50 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'm_age'


class MCast(models.Model):
    cast_id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='cast')
    cast_actor = models.CharField(max_length=45)
    cast_cast = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_cast'


class MComment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='comment')
    comment_userid = models.IntegerField(db_column='comment_userId')  # Field name made lowercase.
    comment_username = models.CharField(db_column='comment_userName', max_length=45)  # Field name made lowercase.
    comment_point = models.IntegerField()
    comment_contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_comment'


class MGender(models.Model):
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='gender', primary_key=True)
    gender_man = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_gender'


class MMovie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=45)
    movie_url = models.TextField()
    movie_aud = models.FloatField(blank=True, null=True)
    movie_net = models.FloatField(blank=True, null=True)
    movie_rep = models.FloatField(blank=True, null=True)
    movie_poster = models.TextField()
    movie_genre = models.IntegerField()
    movie_country = models.IntegerField()
    movie_runtime = models.IntegerField()
    movie_release = models.DateField()
    movie_director = models.CharField(max_length=45, blank=True, null=True)
    movie_age = models.IntegerField()
    movie_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'm_movie'


class MPoint(models.Model):
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='point', primary_key=True)
    point_dir = models.IntegerField()
    point_act = models.IntegerField()
    point_sto = models.IntegerField()
    point_vis = models.IntegerField()
    point_ost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_point'

class Mitem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey('MMovie', on_delete=models.CASCADE, related_name='item')
    user_id = models.IntegerField()
    comment_point = models.IntegerField()
    movie_genre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_item'