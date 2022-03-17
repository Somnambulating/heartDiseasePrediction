from django.urls import path
from django.conf.urls import url
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     url(r'^search-post/$', views.search_post)
# ]

urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]