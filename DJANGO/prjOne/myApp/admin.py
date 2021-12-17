from django.contrib import admin

# Student 모델 임포트
from .models import Student, City

# Register your models here.
# 관리자 페이지에 Student 모델 추가
admin.site.register(Student)
admin.site.register(City)