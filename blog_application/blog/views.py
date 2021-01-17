from django.shortcuts import render, get_object_or_404 
from .models import Post 


def post_list(request): 
    context = {} # context of application. 
    list_of_post = Post.objects.all() # get list of all post. 
    list_of_post = list(list_of_post) # convert it into List of post.
    context['post_list'] = list_of_post 
    return render(request, 'blog/post/list.html', context) # render List of page. 


def post_detail(request, year, month, day, post): 
    context = {}
    post = get_object_or_404(Post, 
                            slug=post, 
                            publish__year = year, 
                            publish__month = month, 
                            publish__day = day, 
                            status='published') # get the object. 

    context['post_details'] = post # details of post added in context. 
    return render(request, 'blog/post/detail.html',context) # responce to html. 
