from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model


UserModel = get_user_model()


def create_user_view(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, template_name='register.html', context=context)


class RegisterUserView(views.CreateView):
    model = UserModel
    fields = ['username', 'password1', 'password2']
    template_name = 'register.html'

    def get_form_class(self):
        return UserCreationForm


class LoginUserView(auth_views.LoginView):
    template_name = 'login-user.html'

    def get_success_url(self):
        return reverse('index')


class LogoutUserView(auth_views.LogoutView):

    http_method_names = ['post', 'options', 'get']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')

