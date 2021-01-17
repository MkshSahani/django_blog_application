from django.db import models
from django.db.models.fields import related
from django.utils import timezone 
from django.contrib.auth.models import User 


class Post(models.Model): 
    STATUS_CHOICES_FOR_POST = (
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) # status of post.. 

    title = models.CharField(max_length=200) # title of post. 
    slug = models.SlugField(max_length=200, unique_for_date='publish') # slug for post. 
    author = models.ForeignKey(User, related_name="post_author", on_delete=models.DO_NOTHING) # author foriegn key. 

    post_text = models.TextField() # post text. 

    created = models.DateTimeField(default=timezone.now) # created on. 
    publish = models.DateTimeField(auto_now_add=True) # publish post. 
    updated = models.DateTimeField(auto_now=True) # updated time and date. 
    status = models.CharField(max_length=50, choices=STATUS_CHOICES_FOR_POST, default='Draft') # choices for post. 

    def __str__(self): 
        return self.title # ger the title of post. 

    