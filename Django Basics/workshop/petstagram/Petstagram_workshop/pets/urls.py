from django.urls import path, include
from Petstagram_workshop.pets import views

urlpatterns = (
    path('add/', views.PetAddView.as_view(), name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('', views.PetDetailsView.as_view(), name='pet details'),
            path('edit/', views.pet_edit, name='pet edit'),
            path('delete/', views.pet_delete, name='pet delete')
        ]
    ))

)