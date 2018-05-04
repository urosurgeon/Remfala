from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog


def allblog(request):
    posts = Blog.objects.all()

    context = {
        'posts': posts,


    }
    return render(request, 'blog/allblog.html', context)


def blogdetail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    context = {
        'post': post
    }
    return render(request, 'blog/blogdetail.html', context)