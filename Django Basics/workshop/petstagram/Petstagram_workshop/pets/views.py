from django.shortcuts import render, get_object_or_404, redirect

from Petstagram_workshop.pets.models import Pet
from .forms import PetForm


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

    context = {
        'pet': pet,
        'photos': pet_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):

    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username, pet_slug):

    return render(request, 'pets/pet-delete-page.html')
