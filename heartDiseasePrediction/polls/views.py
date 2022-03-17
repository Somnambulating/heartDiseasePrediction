from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, "index.html", context)
