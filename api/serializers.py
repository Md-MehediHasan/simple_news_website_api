from rest_framework import serializers
from .models import *



# class SubSectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=SubHeaders
#         fields=['id','title','path']
# class HeadersSerializer(serializers.ModelSerializer):
#     sub_sections=SubSectionSerializer(source='subheaders_ref',many=True,read_only=True)
#     class Meta:
#         model=Headers
#         fields=['id','title','path','has_sub_section','sub_sections']
class NewsPhotoSerializer(serializers.ModelSerializer):
    image_url=serializers.SerializerMethodField()
    class Meta:
        model=NewsPhoto
        fields=['image_url']
    def get_image_url(self,obj):
        request=self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
    
class NewsSerializer(serializers.ModelSerializer):
    files=NewsPhotoSerializer(source='file_reference',many=True,read_only=True)
    upload_file=serializers.ListField(child=serializers.ImageField(),write_only=True)
    class Meta:
        model=News
        fields=['id','news_title','news_content','news_category','created_at','files','upload_file','read_times']

class NewsAsHeading(serializers.ModelSerializer):
    shorten_content=serializers.SerializerMethodField(read_only=True)
    file=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=News
        fields=['id','news_title','shorten_content','news_category','file']
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

    
class AdvetisementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement
        fields='__all__'

class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

