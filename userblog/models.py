# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

#this is to make drop-dropdown
CATEGORY_CHOICES = {
    ('itposts', 'ITPOSTS'),
    ('artposts','ARTPOSTS'),
} #after doing changes to models- do makemigrations

#this is to enable to access the permisssions
from django.contrib.auth.models import Permission

# Create your models here. (place to define our blog Post)
class UserPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete =models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #for category drop-dropdown
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='itposts')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        #we will get a text (string) with a Post title.
