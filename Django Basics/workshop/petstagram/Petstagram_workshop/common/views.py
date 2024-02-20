from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from Petstagram_workshop.common.forms import CommentAddForm, SearchForm
from Petstagram_workshop.photos.models import Photo, Pet, Like, Comment

from pyperclip import copy


def home_page(request):

    pet_photos = Photo.objects.all()
    comment_form = CommentAddForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid() and request.GET:
        pet_photos = pet_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],).distinct()

    context = {
        'photos':       pet_photos,
        'comment_form': comment_form,
        'search_form':  search_form,
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


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentAddForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.to_photo = photo
            instance.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
