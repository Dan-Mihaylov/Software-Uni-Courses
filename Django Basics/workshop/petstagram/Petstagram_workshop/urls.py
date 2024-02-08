from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Petstagram_workshop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstagram_workshop.common.urls')),
    path('accounts/', include('Petstagram_workshop.accounts.urls')),
    path('pets/', include('Petstagram_workshop.pets.urls')),
    path('photos/', include('Petstagram_workshop.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
