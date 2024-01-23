from datetime import datetime

from django.shortcuts import render
from django.urls import reverse


class Person:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def index(request):

    person_1 = Person('Gosho', 'Goshov')
    person_2 = Person('Calypso', 'Seaworthy')

    context = {
        'person_1': person_1,
        'person_2': person_2,
        'person': {
            'first_name': 'Daniel',
            'last_name': 'Mihaylov',
        },
        'person_dict': person_1.__dict__,

        'names': ['Gosho', 'Pesho', 'Laura', 'Maria'],
        'ages': [10, 22, 91, 18],
        'ages_empty': [],

        'date': datetime.today(),
        'get_params': request.GET,
        'post_params': request.POST,

        'reverse_index': reverse('index')


    }

    return render(request, template_name='employees/index.html', context=context)


def employee_details(request, pk):

    context = {
        'employee_pk': pk,
        'type_pk': str(type(pk)),
    }

    return render(request, 'employees/employee_details.html', context=context)
