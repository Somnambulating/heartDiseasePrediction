from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('generic', views.generic, name='generic'),
    path('predict_index', views.predict_index, name='predict_index'),
    path('document_heart_outline', views.document_heart_outline, name='document_heart_outline'),
    path('document_heart_reason', views.document_heart_reason, name='document_heart_reason'),
    
    
    path('predict-post', views.predict_probility, name='predict-post')
]