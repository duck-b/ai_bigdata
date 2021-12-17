from django.db import models

# Create your models here.

# 학생 테이블 모델 정의
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=10)

    def __str__(self):
        return self.s_name

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField(default=0)

    def __str__(self):
        return self.name