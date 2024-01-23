from django.urls import path
from . import views


urlpatterns = (
    path('', views.index, name='index'),
    path('details/<pk>', views.employee_details, name='employee_details'),
)
