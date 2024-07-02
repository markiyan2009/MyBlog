from django.shortcuts import render
from blog.models import Post
# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    context = {
        "posts_list" : posts
    }
    return render(
        request=request,
        template_name="blog/posts_list.html",
        context=context
    )