from django.urls import path
from URLsAndViews.core import views


urlpatterns = (
    path('', views.index, name='index'),
)
