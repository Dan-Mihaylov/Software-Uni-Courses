from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('modelforms', views.index_models, name='index-models'),
    path('modelforms/<int:pk>', views.update_employee, name='update-employee'),
)
