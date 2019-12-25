from django.shortcuts import render

# Create your views here.
from blog.models import PostFile, PostImage, Post


def index(request):
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    posts = Post.objects.all().order_by('-created_date')[:5]
    return render(request, 'home/index.html', {'posts': posts, 'files': files, 'images': images})


def about(request):
    return render(request, 'home/about.html')


def content(request):
    return render(request, 'home/content-news.html')
