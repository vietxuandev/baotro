from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('content', views.content, name='content'),
]
