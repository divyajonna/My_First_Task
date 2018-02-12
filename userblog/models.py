# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

#this is to make drop-dropdown
CATEGORY_CHOICES = {
    ('1', 'ITPOSTS'),
    ('2','ARTPOSTS'),
} #after doing changes to models- do makemigrations


#this is to enable to access the permisssions
from django.contrib.auth.models import Permission
#from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here. (place to define our blog Post)
class UserPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete =models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        #we will get a text (string) with a Post title.


#for category drop-dropdown
category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='itposts')

#to create custom permisssions
class CreatePermission(models.Model):
    class Meta:
        permissions=(
            ("itposts", "IT Posts displayed"),
            ("artposts","Art posts displayed"),
        )
    #contenttype = ContentType.objects.get_for_model(UserPost)
    #username=User.objects.get_or_create(value='1')
