from django import forms
from .models import ImageModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトルを入力'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # 使用するフィールドを指定
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード（確認）'}),
        }