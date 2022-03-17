from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict-post', views.predict_probility, name='predict-post')
]