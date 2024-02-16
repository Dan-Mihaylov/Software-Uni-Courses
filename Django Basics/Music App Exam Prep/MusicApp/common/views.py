from django.shortcuts import render, redirect

from .helpers import check_if_profile_exist, get_profile_object, get_user_albums
from ..account.forms import CreateProfileForm


def home_page(request):

    profile = None
    albums = None
    template = 'common/home-no-profile.html'

    if check_if_profile_exist():
        profile = get_profile_object()
        template = 'common/home-with-profile.html'
        albums = get_user_albums(profile)

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateProfileForm()


    context = {
        'profile': profile,
        'albums': albums,
        'form': form,
    }

    return render(request, template_name=template, context=context)

