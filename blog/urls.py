from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('post-list/', views.post_list, name='post-list'),
    path('image-list/', views.image_list, name='image-list'),
    path('video-list/', views.video_list, name='video-list'),
    path('file-list/', views.file_list, name='file-list'),
    path('post-edit/', views.post_edit, name='post-edit'),
    path('post-new/', views.post_new, name='post-new'),
    path('post-detail/', views.post_detail, name='post-detail'),
    path('image-detail/', views.image_detail, name='image-detail'),
    path('image-new/', views.image_new, name='image-new'),
]
