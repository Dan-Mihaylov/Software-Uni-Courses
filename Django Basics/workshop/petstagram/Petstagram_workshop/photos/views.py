from django.http import HttpResponse
from django.shortcuts import render


def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    return render(request, 'photos/photo-details-page.html')


def photo_edit(request, pk):
    print(pk)
    return render(request, 'photos/photo-edit-page.html')


def photo_delete(request, pk):
    return HttpResponse('delete page')
