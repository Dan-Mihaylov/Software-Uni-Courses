from django.urls import path
from . import views

urlpatterns = [
    path('create/cbv', views.RegisterUserView.as_view(), name='register-cbv'),
    path('create/', views.create_user_view, name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
]