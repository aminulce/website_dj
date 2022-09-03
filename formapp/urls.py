from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.contact, name='form'),
    path('resumeCompare',views.snippet_detail, name = 'snippet'),
]
