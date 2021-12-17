from django.urls import path
from . import views


# 시작페이지 주소와 뷰 한수 연결
urlpatterns = [
    path('', views.index),
    path('sub1/', views.sub1),
    path('sub2/', views.sub2),
    path('sub3/', views.sub3),
    path('sub4/', views.sub4),
    path('sub5/', views.sub5),
    path('sub6/', views.sub6),
    path('numberCon/', views.numberCon),
    path('sub7/', views.sub7),
    path('animalCon/', views.animalCon),
    path('sub8/', views.sub8),
    path('messageCon/', views.messageCon),
    path('sub9/', views.sub9),
    path('calculatorCon/', views.calculatorCon),
    path('sub10/', views.sub10),
    path('sub11/', views.sub11),
    path('sub12/', views.sub12),
    path('all/', views.all),
    path('<id>/detail/', views.detail),
    path('register/', views.register),
    path('registerCon/', views.registerCon),
    path('<id>/wipe/', views.wipe),
    path('<id>/modify/', views.modify),
    path('modifyCon/', views.modifyCon),
    path('city/', views.city),
]
