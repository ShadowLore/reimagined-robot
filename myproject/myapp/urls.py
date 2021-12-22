from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('load', views.load, name='load'),
    path('inference', views.inference, name='inference'),
    path('test1', views.test1, name='test1'),
    path('register', views.register, name='register')
]