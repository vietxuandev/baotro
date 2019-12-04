from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import UserProfile
from blog.forms import PostNewForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post-list.html', {'posts': posts})


def post_edit(request):
    return render(request, 'blog/post-edit.html')


def post_new(request):
    if request.method == 'POST':
        form = PostNewForm(request.POST, request.FILES)
        if form.is_valid():
            print("Ahihi")
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post-list')
    else:
        form = PostNewForm()
    return render(request, 'blog/post-new.html', {'form': form})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post-detail.html', {'post': post})
