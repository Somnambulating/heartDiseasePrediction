from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf
 
# 接收请求数据
def predict(request):
    request.encoding='utf-8'

    if request.POST:
        age = request.POST['age']
        message = message + age
    else:
        message = "failed"
    # sex = request.POST['sex']

    # cp = request.Get['cp']
    # trestbps = request.Get['trestbps']
    # chol = request.Get['chol']
    # fbs	= request.Get['fbs']
    # restecg = request.Get['restecg']
    # thalach = request.Get['thalach']
    # exang = request.Get['exang']
    # oldpeak	= request.Get['oldpeak']
    # slope = request.Get['slope']
    # ca = request.Get['ca']
    # thal = request.Get['thal']

    # message = "without prediction"

    return HttpResponse(message)

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, "index.html", context)
