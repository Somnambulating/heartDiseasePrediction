from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf
 
# 接收请求数据
def predict(request):
    request.encoding='utf-8'
    # request.encoding='utf-8'
    # if 'q' in request.GET and request.GET['q']:
    #     message = '你搜索的内容为: ' + request.GET['q']
    # else:
    #     message = '你提交了空表单'
    # return HttpResponse(message)

    if 'age' in request.GET and request.GET['age']:
        message = '你搜索的内容为: ' + request.GET['age']
    else:
        message = '你提交了空表单'

    sex = request.Get['sex']
    message = message + request.GET['sex']
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
