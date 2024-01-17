# This file is now a frontend-only file

from django.shortcuts import render


def index(request):
    # This part is now removed as it was fetching data from the backend
    # and preparing context for the template.
    # If needed, you can still define frontend-specific logic here.

    # No backend data is passed to the context for rendering the template.
    context = {}

    return render(request, 'pages/index.html', context)


def about(request):
    # This part is now removed as it was fetching data from the backend
    # and preparing context for the template.
    # If needed, you can still define frontend-specific logic here.

    # No backend data is passed to the context for rendering the template.
    context = {}

    return render(request, 'pages/about.html', context)


def services(request):

    context={}

    return render(request, 'pages/services.html', context)



def engagement (request):

    context={}

    return render(request, 'pages/engagement.html', context)