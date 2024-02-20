from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from Petstagram_workshop.pets.models import Pet
from .forms import PetForm, PetEditForm, PetDeleteForm
from ..common.forms import CommentAddForm

from django.views import generic as views


class PetAddView(views.CreateView):
    model = Pet
    fields = '__all__'
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': 1})

    def get_form_class(self):
        return PetForm


class PetDetailsView(views.DetailView):

    model = Pet
    slug_url_kwarg = 'pet_slug'     # Changing the way you pass the slug into the URL (usually it is named just slug)
    context_object_name = 'pet'     # Changing the name of the 'object' so it is accessible in the template as 'pet'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.all()
        context['comment_form'] = CommentAddForm()
        return context

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
