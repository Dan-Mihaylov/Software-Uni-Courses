from django.urls import path, include
from Petstagram_workshop.accounts import views


urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', include(
        [
            path('', views.show_profile_details, name='profile details'),
            path('edit/', views.edit_profile, name='profile edit'),
            path('delete/', views.delete, name='profile delete'),
        ]
    )),
)
