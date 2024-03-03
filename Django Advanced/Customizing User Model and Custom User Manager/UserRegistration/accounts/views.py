from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout as auth_logout, login as auth_login

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from UserRegistration.accounts.forms import CustomUserCreationForm

UserModel = get_user_model()


class RegisterView(views.CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        form = super().form_valid(*args, **kwargs)
        auth_login(self.request, self.object)
        return form


class LoginView(LoginView):

    template_name = 'login.html'

    def get_success_url(self):
        return reverse('index')


class LogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('index')
    http_method_names = ['get', 'post', 'options']
    
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('index')
