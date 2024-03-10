from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.views import generic as views

from Petstagram_workshop.common.forms import CommentAddForm, SearchForm
from Petstagram_workshop.photos.models import Photo, Pet, Like, Comment

from pyperclip import copy


# def home_page(request):
#
#     pet_photos = Photo.objects.all()
#     comment_form = CommentAddForm()
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid() and request.GET:
#         pet_photos = pet_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],).distinct()
#
#     context = {
#         'photos':       pet_photos,
#         'comment_form': comment_form,
#         'search_form':  search_form,
#     }
#
#     return render(request, 'common/home-page.html', context)


class HomePageView(views.ListView):
    # Optimizing DB queries with prefetch related, so you don't hit the DB many times.
    # queryset = Photo.objects.all().prefetch_related('tagged_pets__photos').prefetch_related('likes')

    template_name = 'common/home-page.html'
    paginate_by = 1

    context_object_name = 'photos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentAddForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Photo.objects.all().prefetch_related('tagged_pets__photos').prefetch_related('likes').order_by('-pk')
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            self.request.session['pet_name'] = pet_name
            print(self.request.session['pet_name'])
        else:
            self.request.session['pet_name'] = ''
            print(f'Else statement {self.request.session["pet_name"]}')

        pet_name_session = self.request.session.get('pet_name')

        if pet_name_session:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name_session).distinct()

        return queryset


def like_functionality(request, photo_id: int):

    current_photo = get_object_or_404(Photo, id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=current_photo, user=request.user)
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
            instance.user = request.user
            instance.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
