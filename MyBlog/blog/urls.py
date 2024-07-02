from django.urls import path

import blog.views as blog_views

url_patterns =[
    path("templates\myapp\posts_list.html",blog_views.get_posts, name="posts_list"),
    
] 