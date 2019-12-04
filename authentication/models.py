from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    sex_choices = [
        ('0', 'Nam'),
        ('1', 'Nữ'),
        ('2', 'Khác')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(default='0', max_length=100, choices=sex_choices)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)