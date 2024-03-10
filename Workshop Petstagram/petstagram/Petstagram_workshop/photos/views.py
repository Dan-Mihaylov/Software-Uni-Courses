from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Petstagram_workshop.photos.models import Photo
from .forms import CreatePhotoForm, EditPhotoForm, DeletePhotoForm
from ..common.forms import CommentAddForm


def photo_add(request):

    form = CreatePhotoForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # If the form has a m2m field you need to call this after saving the isntance
        form.save_m2m()

        return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)

# CreatePhotoView don't display the User field


def photo_details(request, pk):

    photo = get_object_or_404(Photo, id=pk)
    comments = photo.comments.all()
    likes = photo.likes.count()
    comment_form = CommentAddForm()

    context = {
        'photo':        photo,
        'comments':     comments,
        'likes':        likes,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, id=pk)

    if request.method == 'GET':
        form = EditPhotoForm(instance=photo)
    else:
        form = EditPhotoForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            instance = form.save()
            return redirect('photo details', pk=pk)

    context = {
        'form':     form,
        'photo':    photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = get_object_or_404(Photo, id=pk)

    if request.method == 'GET':
        form = DeletePhotoForm(instance=photo)
    else:
        form = DeletePhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            instance = form.save(commit=True)
            return redirect('home page')

    context = {
        'form':     form,
        'photo':    photo,
    }

    return render(request, 'photos/photo-delete-page.html', context)
