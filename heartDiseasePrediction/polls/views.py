from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators import csrf
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
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

def document_heart_cure(request):
    context={}
    return render(request,'document_heart_cure.html',context=context)

def document_heart_predict(request):
    context={}
    return render(request,'document_heart_predict.html',context=context)

def document_heart_attention(request):
    context={}
    return render(request,'document_heart_attention.html',context=context)

def signup(request):
    context={}
    return render(request,'signup.html',context=context)

def signup_request(request):
    print("signup_request")
    if request.method == 'POST':
        print("request.POST")
        print(request.POST)
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            print("form.is_valid")
            form.save()
            messages.success(request, f'即将跳转到登录页面')
            return redirect('login')
        else:
            print("form is invalid")
    else:
        print("form = UserRegisterForm()")
        form = UserRegisterForm()
    
    print("failed")
    return render(request, 'index.html')

def login_request(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("user is not None")
            form = login(request,user)
            messages.success(request, f'登录成功，即将跳转至主页')
            print("login success")
            return redirect('index')
        else:
            messages.info(request, f'该账户不存在')
            print("login failed")
    
    print("AuthenticationForm")
    form = AuthenticationForm()
    return render(request, 'index.html', {'form':form,'title':'log in'})

def Login(request):
    context={}
    return render(request,'login.html',context=context)