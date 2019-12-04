from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, 'blog/post-list.html')


def post_edit(request):
    return render(request, 'blog/post-edit.html')


def post_new(request):
    return render(request, 'blog/post-new.html')


def post_detail(request):
    return render(request, 'blog/post-detail.html')