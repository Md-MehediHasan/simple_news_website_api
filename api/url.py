from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    # path('headers/',HeadersView.as_view()),
    path('news/latest/<category>', LatestNews.as_view()),
    path('news/homeNews',GetHomeNews.as_view()),
    path('news/today/<category>',GetTodaysNewsByCategory.as_view()),
    path('news/highest_read/<category>',GetHighestReadByCategory.as_view()),
    path('news/others/<category>',GetOthersNews.as_view()),
    path('news/<category>/<id>/',GetDetailsNews.as_view()),
    path('advertise/',GetAdvertises.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]