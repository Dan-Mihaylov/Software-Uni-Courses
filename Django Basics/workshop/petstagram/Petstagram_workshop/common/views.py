from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from Petstagram_workshop.photos.models import Photo, Pet, Like

from pyperclip import copy


def home_page(request):

    pet_photos = Photo.objects.all()

    context = {
        'photos': pet_photos,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id: int):

    current_photo = get_object_or_404(Photo, id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=current_photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_share(request, photo_id: int):

    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
