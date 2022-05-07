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
    path('document_heart_performance', views.document_heart_performance, name='document_heart_performance'),
    path('document_heart_go_doctor', views.document_heart_go_doctor, name='document_heart_go_doctor'),
    path('document_heart_cure', views.document_heart_cure, name='document_heart_cure'),
    path('document_heart_predict', views.document_heart_predict, name='document_heart_predict'),
    path('document_heart_attention', views.document_heart_attention, name='document_heart_attention'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    
    path('predict-post', views.predict_probility, name='predict-post')
]