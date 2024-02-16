from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from MusicApp.album.models import Album
from MusicApp.common.helpers import get_profile_object


# TODO create a user required and redirect to home page if not user

class AddAlbumView(view.CreateView):
    model = Album
    fields = '__all__'
    template_name = 'album/album-add.html'

    def get_success_url(self):
        return reverse_lazy('home page')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = get_profile_object()
        self.object.save()
        return super().form_valid(form)



class DetailsAlbumView(view.DetailView):
    pass


class EditAlbumView(view.UpdateView):
    pass


class DeleteAlbumView(view.DeleteView):
    pass





