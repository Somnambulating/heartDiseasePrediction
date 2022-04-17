from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('generic', views.generic, name='generic'),
    path('predict_index', views.predict_index, name='predict_index'),
    path('predict-post', views.predict_probility, name='predict-post')
]