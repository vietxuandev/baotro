from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('post-list/', views.post_list, name='post-list'),
    path('post-edit/', views.post_edit, name='post-edit'),
    path('post-new/', views.post_new, name='post-new'),
    path('post-detail/<int:id>', views.post_detail, name='post-detail'),
]
