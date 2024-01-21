from django.shortcuts import render


def show_departments(request):
    return render(request, template_name='departments/departments.html')
