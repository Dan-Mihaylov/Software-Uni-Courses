from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from Petstagram_workshop.photos.models import Photo


def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):

    photo = get_object_or_404(Photo, id=pk)
    comments = photo.comments.all()
    likes = photo.likes.count()

    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    print(pk)
    return render(request, 'photos/photo-edit-page.html')


def photo_delete(request, pk):
    return HttpResponse('delete page')
