from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    template = loader.get_template('templates/index.html')
    return render(request, template, context)
