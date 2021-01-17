from django.contrib import admin
from .models import Post 

# customization for view for Post Model in Admin Panel. 

class PostAdmin(admin.ModelAdmin): 

    list_display = ['title', 'slug', 'author', 'created', 'status']
    list_filter = ['author', 'created', 'publish']

admin.site.register(Post, PostAdmin) # register Post model in admin. 
