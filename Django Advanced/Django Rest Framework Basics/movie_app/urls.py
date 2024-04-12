from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_app.movie_api.urls')),
    path('', include('movie_app.movie.urls')),
]
