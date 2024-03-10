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
        return reverse('profile details', kwargs={'pk': self.request.user.pk})

    def get_form_class(self):
        return PetForm

    def form_valid(self, form):
        pet_instance = form.save(commit=False)
        pet_instance.user = self.request.user
        pet_instance.save()
        return super().form_valid(form)


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


class PetEditView(views.UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    form_class = PetEditForm        # Not just form

    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('pet details', kwargs={'username': 'username', 'pet_slug': self.kwargs['pet_slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['username'] = 'username'
        return context


class PetDeleteView(views.DeleteView):

    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'

    slug_url_kwarg = 'pet_slug'

    form_class = PetDeleteForm

    def get_success_url(self):
        return reverse('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'username'
        return context

    # Easiest way to add pet instance into the form.
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    # Another way to get the initial object filled into the form.
    # def get_initial(self):
    #     return self.object.__dict__


