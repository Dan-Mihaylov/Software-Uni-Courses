from django.urls import path, include
from Petstagram_workshop.accounts import views


urlpatterns = (
    path('register/', views.PetstagramRegisterView.as_view(), name='register'),
    path('login/', views.PetstagramLoginView.as_view(), name='login'),
    path('logout/', views.PetstagramLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include(
        [
            path('', views.show_profile_details, name='profile details'),
            path('edit/', views.PetstagramProfileEditView.as_view(), name='profile edit'),
            path('delete/', views.delete, name='profile delete'),
        ]
    )),
)
