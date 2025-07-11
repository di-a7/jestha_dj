from django.urls import path
from .views import *

urlpatterns = [
   path('home/',home),
   path('aboutus/',aboutus),
   path('index/',index),
   path('contact/',contact),
   path('todolist/',todolist),
]

def add():
   pass
