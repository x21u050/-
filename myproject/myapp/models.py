from django.db import models
from django.contrib.auth.models import User

class ImageModel(models.Model):
    title = models.CharField(max_length=100)  # 画像のタイトル
    image = models.ImageField(upload_to='images/')  # 画像ファイルのフィールド
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)  # ユーザーとの関連付け
    
    def __str__(self):
        return self.title
