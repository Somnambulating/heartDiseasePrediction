from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "index.html", ctx)

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, "index.html", context)
