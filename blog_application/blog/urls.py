from django.urls import path, re_path
from django.conf import urls 
from . import views 

urlpatterns = [
    path('', views.post_list, name="PostList"), 
    re_path('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w+])/$', views.post_detail, name="PostDetails"), 
]
