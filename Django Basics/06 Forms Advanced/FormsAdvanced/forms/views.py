from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import PersonForm, UpdatePersonForm
from .models import Person


def index(request):
    form = PersonForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/index.html', context)


def create_person(request):
    form = PersonForm(request.user, request.POST, request.FILES,)

    if form.is_valid():
        instance = form.save()

        return render(request, 'forms/person_added.html', context={'person': instance})

    return redirect('index')


class ListPeople(ListView):
    model = Person
    template_name = 'forms/list_objects.html'
    context_object_name = 'people'

    paginate_by = 4


def update_user(request, user_id):

    user = get_object_or_404(Person, id=user_id)

    form = UpdatePersonForm(instance=user)

    if request.method == 'POST':
        form = UpdatePersonForm(request.user, request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list-people')

    context = {
        'form': form,
        'user_id': user_id,
    }

    return render(request, 'forms/update_person.html', context)