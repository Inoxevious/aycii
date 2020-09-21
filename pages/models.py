from django.db import models
from account.models import *
# Create your models here.


class HomePageBanners(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    author = models.ForeignKey(AccountUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    title_font_size =models.IntegerField(null=True ,blank=True, default=50)
    summary =models.CharField(max_length=100,null=True ,blank=True)
    tag_text =models.TextField(null=True ,blank=True)
    tag_text_font_size =models.IntegerField(null=True ,blank=True, default=20)
    isActive = models.BooleanField(default=True)
    isHomeArticle = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class HomePageTestimonials(models.Model):
    author = models.ForeignKey(AccountUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video_link = models.TextField(null=True ,blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    summary =models.CharField(max_length=100,null=True ,blank=True)
    tag_text =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isHomeArticle = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title