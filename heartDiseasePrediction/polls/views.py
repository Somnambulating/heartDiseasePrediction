from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from simplejson import load

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    # template = loader.get_template('/templates/index.html')
    return render(request, "index.html", context)
