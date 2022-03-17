from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf
import sys

from predict.machine_learning import Predict 
prediction = Predict()
prediction.init()

# 接收请求数据
def predict_probility(request):
    request.encoding='utf-8'

    if request.POST:
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs	= int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak	= int(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])

        info = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        result = prediction.predict(info)
        message = "患得心脏病的几率为: " + result
    else:
        message = "failed"

    return HttpResponse(message)

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, "index.html", context)
