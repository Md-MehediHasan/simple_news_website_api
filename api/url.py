from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    
    path('news/latest/<category>', LatestNews.as_view()),
    path('news/homeNews',GetHomeNews.as_view()),
    path('news/today/<category>',GetTodaysNewsByCategory.as_view()),
    path('news/highest_read/<category>',GetHighestReadByCategory.as_view()),
    path('news/others/<category>',GetOthersNews.as_view()),
    path('news/<id>/',GetDetailsNews.as_view()),
    path('news/update/read_count/<pk>/',UpdateNewsRead.as_view()),
    path('news/search/<topic>/',GetNewsByTopic.as_view()),
    path('news/topic/latest/',GetLatestTopics.as_view()),
    path('advertise/',GetAdvertises.as_view()),
]