from django.urls import path, include
from Petstagram_workshop.common import views


urlpatterns = (
    path('', views.HomePageView.as_view(), name='home page'),
    path('like/<int:photo_id>', views.like_functionality, name='like'),
    path('share/<int:photo_id>', views.copy_link_to_share, name='share'),
    path('comment/<int:photo_id>', views.add_comment, name='comment')
)
