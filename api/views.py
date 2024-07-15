from django.shortcuts import render
from api.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
from rest_framework.generics import UpdateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from django.db.models import Q 
from datetime import date
from pytz import timezone as tz
from django.db.models import Q
from rest_framework.permissions import AllowAny
from django.db.models import Count
import urllib.parse



class LatestNews(ListAPIView):
            queryset=News.objects.filter(publishing_status=True)
            def list(self,request,category):
                    category=category.lower()
                    category=category.replace('+',' ')
                    latest=[]
                    if category=='all':
                             latest.extend(list(News.objects.filter(publishing_status=True).order_by('-created_at'))[:6]) 
                    if category is not None:
                      latest.extend(list(News.objects.filter(Q(news_category=category) & Q(publishing_status=True)).order_by('-created_at'))[:6])
                    data=NewsAsHeading(latest,many=True,context={'request':request}).data
                    return Response(data,status=status.HTTP_200_OK)
             
             
             
             
class GetHomeNews(ListAPIView):
       queryset=News.objects.filter(publishing_status=True)
       def list(self, request):
              news=list(News.objects.filter(publishing_status=True).order_by('-created_at'))[:8]
              opinions=list(News.objects.filter(Q(news_category='opinions') & Q(publishing_status=True)).order_by('-created_at'))[1:7]
              politics=list(News.objects.filter(Q(news_category='bangladesh & politics')&Q(publishing_status=True)).order_by('-created_at'))[1:7]
              economics=list(News.objects.filter(Q(news_category='bangladesh & economics') & Q(publishing_status=True)).order_by('-created_at'))[1:7]
              sports=list(News.objects.filter(Q(news_category__icontains='sports') & Q(publishing_status=True)).order_by('-created_at'))[1:7]
              news.extend(opinions)
              news.extend(politics)
              news.extend(economics)
              news.extend(sports)
              data=NewsAsHeading(news,many=True,context={'request':request}).data
              return Response(data,status=status.HTTP_200_OK)
       
       
       
class GetTodaysNewsByCategory(ListAPIView):
       queryset=News.objects.filter(publishing_status=True)
       def list(self,request,category):
               category=category.lower()
               newsByCategory=News.objects.filter(Q(news_category=category) & Q(publishing_status=True))
               todays_news=[]
               for item in newsByCategory:
                      if item.created_at.day==date.today().day:
                             todays_news.append(item)
               data=NewsAsHeading(todays_news,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
        
        
class GetHighestReadByCategory(ListAPIView):
       queryset=News.objects.filter(publishing_status=True)
       def list(self,request,category):
               category=category.lower()
               category=category.replace('+',' ')
               highestReads=[]
               if category=='all':
                  highestReads.extend(list(News.objects.filter(publishing_status=True).order_by('-read_times'))[:6])
               else:
                highestReads.extend(list(News.objects.filter(Q(news_category=category) & Q(publishing_status=True)).order_by('-read_times'))[:6])
               data=NewsAsHeading(highestReads,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
        
        
        
class GetOthersNews(ListAPIView):
       queryset=News.objects.filter(publishing_status=True)
       def list(self,request,category):
               category=category.replace('+',' ')
               nonCategory=News.objects.filter(~Q(news_category=category) & Q(publishing_status=True)).order_by('read_times')
               data= NewsAsHeading(nonCategory,many=True,context={'request':request}).data
               return Response(data,status=status.HTTP_200_OK)
        
        
        
class UpdateNewsRead(APIView):
       permission_classes=[AllowAny]
       serializer_class=ReadCountUpdateSerializer
       queryset=News.objects.all()
       def patch(self, request,pk):
             try:
               target_news=News.objects.get(pk=pk)
               target_news.read_times =target_news.read_times +1
               target_news.save()
               return Response('Updated successfully')
             except:
                    return Response('News not found')
                     
                      
class GetAdvertises(ListAPIView):
       queryset=list(Advertisement.objects.filter(publishing_status=True))[:20]
       serializer_class=AdvetisementSerializer
       
       
class GetDetailsNews(RetrieveAPIView):
       queryset=News.objects.filter(publishing_status=True)
       serializer_class=NewsSerializer
       def get(self, request,id):
        target_news= News.objects.filter(id=id).first()
        data=NewsSerializer(target_news,context={'request':request}).data
        return Response(data,status=status.HTTP_200_OK)
 
class GetLatestTopics(APIView):
       def get(self,request):
              relavant_topic=[]
              latest_news=list(News.objects.filter(publishing_status=True).order_by('-created_at'))[:5]
              for item in latest_news:
                     if item.relavant_topics is not None:
                            topics=item.relavant_topics.split(',')
                            for topic  in topics:
                                   if topic not in relavant_topic:
                                          relavant_topic.append(topic)
             
              return Response(relavant_topic[:10],status=status.HTTP_200_OK)
 
class GetNewsByTopic(ListAPIView):
        queryset=News.objects.filter(publishing_status=True)
        def list(self, request, topic):
             topic=urllib.parse.unquote(topic)
             matched_news=News.objects.filter(relavant_topics__icontains=topic)
             data=NewsSerializer(matched_news,many=True,context={'request':request}).data
             return Response(data,status=status.HTTP_200_OK)
              
        

                