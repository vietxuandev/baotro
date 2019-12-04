from django.contrib import admin

# Register your models here.
from authentication.models import UserProfile
from blog.models import Post

admin.site.register(UserProfile)
admin.site.register(Post)