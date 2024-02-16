from django.urls import path
from . import views


urlpatterns = [
    path('details/', views.DetailsProfileView.as_view(), name='details profile'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete profile'),
]

