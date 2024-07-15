from rest_framework import serializers
from .models import *


class NewsPhotoSerializer(serializers.ModelSerializer):
    image_url=serializers.SerializerMethodField()
    class Meta:
        model=NewsPhoto
        fields=['image_url','image']
    def get_image_url(self,obj):
        request=self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
    
    
class NewsSerializer(serializers.ModelSerializer):
    files=NewsPhotoSerializer(source='file_reference',many=True,read_only=True)
    upload_file=serializers.ListField(child=serializers.FileField(),write_only=True,required=False)
    
    class Meta:
        model=News
        fields=['id','written_by','news_title','news_content','news_category','created_at','files','upload_file','publishing_status','relavant_topics']
   
  
       

class NewsAsHeading(serializers.ModelSerializer):
    shorten_content=serializers.SerializerMethodField(read_only=True)
    file=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=News
        fields=['id','news_title','shorten_content','news_category','file','read_times']
    def get_shorten_content(self,obj):
        return obj.news_content[0:90]+''+".."
    def get_file(self,obj):
        context=self.context
        image=NewsPhoto.objects.filter(news_reference=obj).first()
        return NewsPhotoSerializer(image,context=context).data
    
    
    
class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Opinion
        fields=['id','news_title','news_content','news_category','files','upload_file','read_times','speaker']



class OpinionAsHeading(serializers.ModelSerializer):
    shorten_content=serializers.SerializerMethodField(read_only=True)
    file=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Opinion
        fields=['id','news_title','shorten_content','news_category','file','speaker']
    def get_shorten_content(self,obj):
        return obj.news_content[0:90]+''+".."
    def get_file(self,obj):
        context=self.context
        image=NewsPhoto.objects.filter(news_reference=obj).first()
        return NewsPhotoSerializer(image,context=context).data
    
    
    
class ReadCountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['read_times']

    
    
class AdvetisementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement
        fields=['image','position','url','publishing_status']
class RelavantTopicSerializer(serializers.Serializer):
    relavant_topic=serializers.CharField()
        



