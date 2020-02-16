from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from authentication.models import UserProfile
from blog.models import Post, PostImage, Image


class ImageForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'multiple': True}))


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập tên bài đăng'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập mô tả bài viết'
                }
            ),
        }


class PostNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description', 'content')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập tên bài đăng'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'custom-file-input'
                }
            ),
            # 'video_link': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Nhập đường dẫn liên kết video'
            #     }
            # ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập mô tả bài viết'
                }
            )
        }


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'birthday', 'gender', 'phone_number')
