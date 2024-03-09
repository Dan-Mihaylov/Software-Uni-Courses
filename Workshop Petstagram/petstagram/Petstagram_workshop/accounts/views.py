from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views

from .forms import PetstagramUserCreationForm


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


def login(request):
    return render(request, 'accounts/login-page.html')


class PetstagramLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True


# TODO: Create a LogoutView to be consistent with the other Views
def logout(request):
    auth_logout(request)
    return redirect('home page')


class PetstagramLogoutView(auth_views.LogoutView):
    pass


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
