from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_person/', views.create_person, name='create-person'),
    path('list/people/', views.ListPeople.as_view(), name='list-people'),
    path('update_user/<int:user_id>', views.update_user, name='update-user'),
]
