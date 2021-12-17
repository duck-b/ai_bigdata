from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('login/', views.index),
    path('loginCon/', views.loginCon),
    path('user/', views.user),
    path('user/search/', views.search),
    path('user/search/<webtoonid>/createCon/', views.createSearchCon),
    path('user/search/<webtoonid>/deleteCon/', views.deleteSearchCon),
    path('user/webtoon/<webtoonid>/', views.webtoon),
    path('user/webtoon/<webtoonid>/create/', views.createComment),
    path('user/webtoon/<webtoonid>/createCon/', views.createCommentCon),
    path('user/webtoon/<webtoonid>/update/', views.updateComment),
    path('user/webtoon/<webtoonid>/updateCon/', views.updateCommentCon),
    path('user/webtoon/<webtoonid>/deleteCon/', views.deleteCommentCon),
    path('user/<week>/', views.userWeek),
]