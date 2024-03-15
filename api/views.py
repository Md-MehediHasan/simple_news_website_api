from django.shortcuts import render
from api.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
from rest_framework.generics import ListCreateAPIView,CreateAPIView,ListAPIView,RetrieveAPIView
from django.db.models import Q 
from datetime import date
from pytz import timezone as tz
from django.db.models import Q



class LatestNews(ListAPIView):
            queryset=News.objects.all()
            def list(self,request,category):
                    category=category.lower()
                    latest=[]
                    if category=='all':
                             latest.extend(News.objects.order_by('-created_at')) 
                    if category is not None:
                      latest.extend(News.objects.filter(news_category=category).order_by('-created_at'))
                    data=NewsAsHeading(latest,many=True,context={'request':request}).data
                    return Response(data,status=status.HTTP_200_OK)
class GetHomeNews(ListAPIView):
       queryset=News.objects.all()
       def list(self, request):
              highest_read=News.objects.filter(~Q(news_category='opinions')).order_by('read_times')
              opinions=Opinion.objects.filter(news_category='opinions').order_by('read_times')  
              data=NewsAsHeading(highest_read,many=True,context={'request':request}).data
              data.extend(OpinionAsHeading(opinions,many=True,context={'request':request}).data)
              return Response(data,status=status.HTTP_200_OK)
class GetTodaysNewsByCategory(ListAPIView):
       queryset=News.objects.all()
       def list(self,request,category):
               category=category.lower()
               newsByCategory=News.objects.filter(news_category=category)
               todays_news=[]
               for item in newsByCategory:
                      if item.created_at.day==date.today().day:
                             todays_news.append(item)
               data=NewsAsHeading(todays_news,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
class GetHighestReadByCategory(ListAPIView):
       queryset=News.objects.all()
       def list(self,request,category):
               category=category.lower()
               if category=='politics' or category=='economics' or category=='report':
                      category=f'bangladesh & {category}'
               newsByCategory=News.objects.filter(news_category=category).order_by('-read_times')
               data=NewsAsHeading(newsByCategory,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
class GetOthersNews(ListAPIView):
       queryset=News.objects.all()
       def list(self,request,category):
               category=category.lower()
               print(category)
               nonCategory=News.objects.filter(~Q(news_category=category)).order_by('read_times')
               data= NewsAsHeading(nonCategory,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
                      
                      
class GetAdvertises(ListAPIView):
       queryset=Advertisement.objects.all()
       serializer_class=AdvetisementSerializer
class GetDetailsNews(RetrieveAPIView):
       queryset=News.objects.all()
       serializer_class=NewsSerializer
       def get(self, request,category,id):
        target_news= News.objects.filter(Q(news_category=category) &Q(id=id)).first()
        data=NewsSerializer(target_news,context={'request':request}).data
        return Response(data,status=status.HTTP_200_OK)
              
        
class LoginView(CreateAPIView):
        serializer_class=LoginDataSerializer
        def post(self, request, *args, **kwargs):
                username=request.data['username']
                password=request.data['password']
                user=authenticate(username=username,password=password)
                if user:
                       data= login(request,user)
                       print(data)
                       return Response("Login Sucessfull",status=status.HTTP_200_OK)
                if user is None:
                        return Response("Credential does not matched",status=status.HTTP_401_UNAUTHORIZED
                                        )
class LogoutView(ListAPIView):
        def list(self, request, *args, **kwargs):
               logout(request)
               return Response('Successfully logged out',status=status.HTTP_202_ACCEPTED)
                