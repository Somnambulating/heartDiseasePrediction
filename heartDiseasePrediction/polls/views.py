from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf
import sys

sys.path.append("..")
from predict.machine_learning import Predict 

# 接收请求数据
def predict_probility(request):
    request.encoding='utf-8'
    prediction = Predict()
    prediction.init()

    if request.POST:
        age = int(request.POST['age'])
        sex = 0
        if request.POST['sex'] == "女":
            sex = 1
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs	= int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak	= float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])

        info = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        result = prediction.predict(info)

    if sex == 0:
        sex = "男"
    else:
        sex = "女"

    context = {'age':age, 'sex':sex, 'cp':cp, 'trestbps':trestbps, \
        'chol':chol, 'fbs':fbs, 'restecg':restecg, 'thalach':thalach, \
        'exang':exang, 'oldpeak':oldpeak, 'slope':slope, 'ca':ca, 'thal': thal, \
        'result': str(round(result*100, 2))}
    return render(request, "result.html", context)
    # return HttpResponse(message)

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, "index.html", context)

def predict_index(request):
    context={}
    return render(request,'predict_index.html',context=context)

def contact(request):
    context={}
    return render(request,'contact.html',context=context)

def elements(request):
    context={}
    return render(request,'elements.html',context=context)

def generic(request):
    context={}
    return render(request,'generic.html',context=context)

def document_heart_outline(request):
    context={}
    return render(request,'document_heart_outline.html',context=context)

def document_heart_reason(request):
    context={}
    return render(request,'document_heart_reason.html',context=context)

def document_heart_performance(request):
    context={}
    return render(request,'document_heart_performance.html',context=context)

def document_heart_go_doctor(request):
    context={}
    return render(request,'document_heart_go_doctor.html',context=context)
