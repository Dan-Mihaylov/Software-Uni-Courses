from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_introduction_01.tasks.models import Task, Recommendation
from django_introduction_01.tasks.forms import RecommendationForm


def index(request):
    context = {
        'recommendations': Recommendation.objects.all()
        }

    if request.method == 'POST':
        # Process the form data
        context['form'] = RecommendationForm(request.POST)

        if context['form'].is_valid():
            username = context['form'].cleaned_data['name']
            recommendation = context['form'].cleaned_data['recommendation']

            Recommendation.objects.create(user_name=username, recommendation=recommendation)

    context['form'] = RecommendationForm()

    return render(request, template_name='tasks/index.html', context=context)


def tasks(request):
    context = {
        'tasks': Task.objects.all(),
        'no_tasks': 'There are no tasks at the moment',
    }

    return render(request, template_name='tasks/tasks.html', context=context)

