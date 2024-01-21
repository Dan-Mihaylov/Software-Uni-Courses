from django.urls import path

from URLsAndViews.departments import views


urlpatterns = (
    path('departments/',views.show_departments, name='show_departments'),
)

