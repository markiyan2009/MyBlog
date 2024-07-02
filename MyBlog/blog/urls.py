from django.urls import path

import blog.views as blog_views

urlpatterns =[
    path("templates\myapp\posts_list.html",blog_views.get_posts, name="posts_list"),
    
] 