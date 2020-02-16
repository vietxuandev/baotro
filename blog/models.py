from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
import os

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    type_choices = [
        ('0', 'Tin trung tâm'),
        ('1', 'Tin trong tỉnh'),
        ('2', 'Hoàn cảnh cần giúp đỡ'),
        ('3', 'Thông tin chỉ đạo, điều hành'),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    video_link = models.URLField(max_length=2000, blank=True)
    description = models.CharField(max_length=500, blank=True)
    content = RichTextField(blank=True, null=True)
    type = models.CharField(default='0', max_length=100, choices=type_choices)
    created_date = models.DateTimeField(default=timezone.now)

    # published_date = models.DateTimeField(blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title


class PostVideo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_link = models.URLField(max_length=2000)
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    # published_date = models.DateTimeField(blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # image = models.ImageField()
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    # published_date = models.DateTimeField(blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def default_image(self):
        return Image.objects.filter(post_image=self).first()

    def __str__(self):
        return self.title


class Image(models.Model):
    post_image = models.ForeignKey(PostImage, on_delete=models.CASCADE)
    image = models.ImageField()


class PostFile(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    number = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    file = models.FileField()
    created_date = models.DateTimeField(default=timezone.now)

    # published_date = models.DateTimeField(blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def filename(self):
        return os.path.basename(self.file.name)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def __str__(self):
        return self.name
