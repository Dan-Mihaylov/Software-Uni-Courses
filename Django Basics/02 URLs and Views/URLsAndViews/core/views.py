from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index_no_template(request, *args, **kwargs):

    return HttpResponse(
        "<h1>It Works</h1>"
    )


def index(request, *args, **kwargs):
    context = {
        "title": "Request data",
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": request.user,
    }

    return render(request, 'core/index.html', context)


def redirect_to_google(request):
    return redirect("https://google.com")


def redirect_to_index(request):
    return redirect('index_no_params')


def redirect_to_index_with_params(request):
    return redirect('index_with_pk_and_slug', pk=20, slug="Pesho")


def index_json(request, *args, **kwargs):
    content = {
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": str(request.user),
    }

    return JsonResponse(
        content,
    )


def raise_error(request):
    return HttpResponseNotFound(
        status=404,
    )


def raise_exception(request):
    raise Http404
