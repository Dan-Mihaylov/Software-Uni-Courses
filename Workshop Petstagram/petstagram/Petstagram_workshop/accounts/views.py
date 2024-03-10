from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from .forms import PetstagramUserCreationForm, PetstagramProfileEditForm, PetstagramChangeForm
from .mixins import ProfileOwnerRequiredMixin
from .models import Profile

UserModel = get_user_model()


class PetstagramRegisterView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = PetstagramUserCreationForm

    def get_success_url(self):
        return reverse('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        auth_login(self.request, form.instance)
        return result


class PetstagramLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True


class PetstagramLogoutView(auth_views.LogoutView):
    pass


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


class PetstagramProfileEditView(ProfileOwnerRequiredMixin, views.UpdateView):
    form_class = PetstagramProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            'profile details', kwargs={
                'pk': self.object.pk,
            }
        )


def delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
