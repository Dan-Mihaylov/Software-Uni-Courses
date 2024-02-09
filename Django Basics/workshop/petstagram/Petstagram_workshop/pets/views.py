from django.shortcuts import render, get_object_or_404, redirect

from Petstagram_workshop.pets.models import Pet
from .forms import PetForm, PetEditForm, PetDeleteForm
from ..common.forms import CommentAddForm


def pet_add(request):

    form = PetForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return redirect('profile details', 1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):

    pet = get_object_or_404(Pet, slug=pet_slug)
    pet_photos = pet.photos.all()
    comment_form = CommentAddForm()

    context = {
        'pet':          pet,
        'photos':       pet_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):

    pet = get_object_or_404(Pet, slug=pet_slug)

    form = PetEditForm(request.POST or None, instance=pet)
    if form.is_valid():
        instance = form.save()
        return redirect('pet details', username, pet_slug)

    context = {
        'form':     form,
        'username': username,
        'pet':      pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):

    pet = get_object_or_404(Pet, slug=pet_slug)

    form = PetDeleteForm(request.POST or None, instance=pet)

    if form.is_valid():
        instance = form.save(commit=True)
        return redirect('profile details', pk=1)
        # This pk = 1 is going to be the user.pk when we have users

    context = {
        'pet':      pet,
        'username': username,
        'form':     form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
