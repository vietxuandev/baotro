from django.shortcuts import render

# Create your views here.
from blog.models import PostFile, PostImage, Post


def index(request):
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    posts = Post.objects.all().order_by('-created_date')[:5]
    posts_0 = Post.objects.filter(type="0").order_by('-created_date')[:4]
    posts_1 = Post.objects.filter(type="1").order_by('-created_date')[:4]
    posts_2 = Post.objects.filter(type="2").order_by('-created_date')[:4]
    posts_3 = Post.objects.filter(type="3").order_by('-created_date')[:4]
    return render(request, 'home/index.html', {'posts': posts, 'files': files, 'images': images, 'posts_0':posts_0,'posts_1':posts_1,'posts_2':posts_2,'posts_3':posts_3})


def about(request):
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'home/about.html', {'files': files, 'images': images})


def org_chart(request):
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'home/org-chart.html', {'files': files, 'images': images})


def content(request):
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'home/content-news.html', {'files': files, 'images': images})
