from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class Headers(models.Model):
    title=models.CharField(max_length=50)
    path=models.CharField(max_length=50)
    has_sub_section=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title
class SubHeaders(models.Model):
    referece_header=models.ForeignKey(Headers,on_delete=models.CASCADE,related_name='subheaders_ref')
    title=models.CharField(max_length=50)
    path=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title


new_category_choices=[
    ('bangladesh & politics','Bangladesh & politics'),
    ('angladesh & economics','Bangladesh & economics'),
    ('bangladesh & report','Bangladesh & report'),
    ('national','National'),
    ('international','International'),
    ('sports & cricket','Sports & cricket'),
    ('sports & football','Sports & football'),
      ('opinions','Opinions'),
    ('jobs','Jobs'),
]
ad_position_choices=[
        ('Insection_ad','InSection_ad'),
        ('Top','Top'),
        ('Sidebar','Sidebar')
    ]

class User(AbstractUser):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    position=models.CharField(max_length=50)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','position']
    def __str__(self):
        return self.email

class News(models.Model):
    writter=models.ForeignKey(User,on_delete=models.CASCADE)
    news_title=models.CharField(max_length=100)
    news_category=models.CharField(max_length=100,choices=new_category_choices,null=True)
    news_content=models.CharField(max_length=50000,null=True)
    created_at=models.DateTimeField(default=now(),null=True)
    read_times=models.IntegerField(null=True)
    written_by=models.CharField(max_length=150,null=True)
    publishing_status=models.BooleanField(default=False,null=True)
    relavant_topics=models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.news_title
   
class NewsPhoto(models.Model):
    news_reference=models.ForeignKey(News,on_delete=models.CASCADE,related_name='file_reference')
    image=models.ImageField()
    
class Opinion(News):
    speaker=models.CharField(max_length=50)
    def __str__(self):
        return self.speaker
class Advertisement(models.Model):
    image=models.FileField(upload_to='advertisement')
    position=models.CharField(max_length=50,choices=ad_position_choices)
    url=models.CharField(max_length=100,null=True)
    publishing_status=models.BooleanField(default=False,null=True)


