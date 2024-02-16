from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MusicApp.common.urls')),
    path('album/', include('MusicApp.album.urls')),
    path('profile/', include('MusicApp.account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

