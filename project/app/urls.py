from django.urls import path
from .views import *


urlpatterns = [
    path("",show,name="index"),
    path("class/",class_detail,name="class"),
]