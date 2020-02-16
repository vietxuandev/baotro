from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import UserProfile
from blog.forms import PostNewForm, ImageForm, PostImageForm
from blog.models import Post, PostImage, PostVideo, PostFile, Image


def post_list(request):
    type = request.GET.get('type')
    if type:
        posts_page =Post.objects.filter(type=str(type)).order_by('-created_date')
    else:
        posts_page = Post.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_page, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/post-list.html', {'posts': posts, 'files': files, 'images': images})


def post_edit(request):
    return render(request, 'blog/post-edit.html')


def post_new(request):
    if request.method == 'POST':
        form = PostNewForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post-list')
    else:
        form = PostNewForm()
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/post-new.html', {'form': form, 'files': files, 'images': images})


def post_detail(request):
    post_id = request.GET.get('id', 1)
    post = Post.objects.get(id=post_id)
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/post-detail.html', {'post': post, 'files': files, 'images': images})


def image_detail(request):
    post_id = request.GET.get('id', 1)
    post = PostImage.objects.get(id=post_id)
    images_detail = Image.objects.filter(post_image_id=post_id)
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/image-detail.html', {'post': post, 'images_detail': images_detail, 'files': files, 'images': images})


def image_list(request):
    posts_page = PostImage.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_page, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/image-list.html', {'posts': posts, 'files': files, 'images': images})


def video_list(request):
    posts_page = PostVideo.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_page, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/video-list.html', {'posts': posts, 'files': files, 'images': images})


def file_list(request):
    posts = PostFile.objects.all().order_by('-created_date')
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/file-list.html', {'posts': posts, 'files': files, 'images': images})


def image_new(request):
    if request.method == 'POST':
        post_image_form = PostImageForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        if image_form.is_valid() and post_image_form.is_valid():
            post_image = post_image_form.save(commit=False)
            post_image.author = request.user
            post_image.save()
            for file in files:
                Image.objects.create(post_image=post_image, image=file)
            return redirect('blog:image-list')
    else:
        image_form = ImageForm()
        post_image_form = PostImageForm()
    files = PostFile.objects.all().order_by('-created_date')[:5]
    images = PostImage.objects.all().order_by('-created_date')[:8]
    return render(request, 'blog/image-new.html', {'image_form': image_form, 'post_image_form': post_image_form, 'files': files, 'images': images})
