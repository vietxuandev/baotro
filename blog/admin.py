from django.contrib import admin

# Register your models here.
from blog.models import Post, PostImage, PostVideo, PostFile, Image

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostVideo)
admin.site.register(PostFile)
admin.site.register(Image)