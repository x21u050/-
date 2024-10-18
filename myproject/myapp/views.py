from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ImageModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
import subprocess
from django.contrib import messages
from django.contrib.auth.models import User


@login_required  # ログインが必要なビューにする
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()  # 保存
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = ImageModel.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'images': images})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後に自動的にログイン
            return redirect('login')  # ログインにリダイレクト
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def dashboard_view(request):
    return render(request, 'user_dashboard.html')

def start_ai_app(request):
    # ユーザーに関連する顔写真を取得
    images = ImageModel.objects.filter(user=request.user)
    
    # データベースの画像が存在するか確認
    if not images.exists():
        return render(request, 'error.html', {'message': '顔写真が登録されていません。'})
    
    # 画像ファイルのパスをリスト化
    image_paths = [img.image_file.path for img in images]
    
    # AIアプリを起動し、画像ファイルを渡す（サンプルコード: subprocessで外部AIアプリを呼び出す）
    try:
        # 例：AIアプリの実行コマンド（画像パスを引数として渡す）
        subprocess.run(['python', 'path_to_ai_app.py'] + image_paths, check=True)
    except subprocess.CalledProcessError as e:
        return render(request, 'error.html', {'message': 'AIアプリの起動に失敗しました。'})
    
    # 処理後にリダイレクト
    return render(request, 'success.html', {'message': 'AIアプリが正常に起動しました。'})

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # ユーザーを削除する
        messages.success(request, 'アカウントが削除されました。')
        return redirect('account_deleted')  # 削除後にリダイレクトするページ
    return render(request, 'delete_account.html')

def account_deleted(request):
    return render(request, 'account_deleted.html')

def home(request):
    return render(request, 'user_dashboard.html')