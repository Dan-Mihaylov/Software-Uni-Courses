from django import forms
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic as views

from ClassBasedViewsAdvanced.web.models import Car


class FilterCarForm(forms.Form):
    car_make = forms.CharField(
        max_length=30,
        required=False,
    )

    engine_type = forms.ChoiceField(
        choices=Car.ENGINE_CHOICES,
        required=False,
    )


class IndexView(views.ListView):
    model = Car
    template_name = 'web/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Available Cars'

        context['search_form'] = FilterCarForm(self.request.GET or None)    # to add the previous search data

        return context

    def get_paginate_by(self, queryset):
        paginate_by = 5
        return paginate_by

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filter_options(queryset)
        return queryset

    def apply_filter_options(self, queryset):

        if self.request.GET['car_make'] and self.request.GET['engine_type']:
            make = self.request.GET.get('car_make', '')
            engine = self.request.GET.get('engine_type', '')
            query = Q(make__icontains=make) & Q(engine_type__icontains=engine)

        elif self.request.GET['car_make']:
            make = self.request.GET.get('car_make', '')
            query = Q(make__icontains=make)

        else:
            engine = self.request.GET.get('engine_type', '')
            query = Q(engine_type__icontains=engine)

        queryset = queryset.filter(query)

        return queryset



