from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def logout(request):
    return HttpResponse('Logout Page')


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
