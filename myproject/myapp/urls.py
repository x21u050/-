from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import delete_account

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # ダッシュボード用ビュー
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('start-ai/', views.start_ai_app, name='start_ai_app'),
    path('delete_account/', delete_account, name='delete_account'),
    path('account_deleted/', views.account_deleted, name='account_deleted'),
    path('', views.home, name='home'),
]



