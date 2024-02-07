from django.shortcuts import render
from Petstagram_workshop.photos.models import Photo, Pet


def home_page(request):

    # Get all Photo objects and pass them as a context
    return render(request, 'common/home-page.html')
