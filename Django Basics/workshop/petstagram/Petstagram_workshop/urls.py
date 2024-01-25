from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('Petstagram_workshop.common.urls')),
    path('accounts/', include('Petstagram_workshop.accounts.urls')),
    path('pets/', include('Petstagram_workshop.pets.urls')),
    path('photos/', include('Petstagram_workshop.photos.urls')),
)
