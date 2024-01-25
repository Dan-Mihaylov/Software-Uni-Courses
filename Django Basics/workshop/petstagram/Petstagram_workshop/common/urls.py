from django.urls import path, include
from Petstagram_workshop.common import views


urlpatterns = (
    path('', views.home_page, name='home page'),
)
