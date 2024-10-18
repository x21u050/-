from django.contrib import admin
from .models import ImageModel
# Register your models here.

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'image')  # 管理画面で表示するフィールド
    search_fields = ('title', 'user__username')  # 検索フィールドにユーザー名を追加
    list_filter = ('user',)  # ユーザーでフィルタリング可能に

admin.site.register(ImageModel, ImageModelAdmin)
