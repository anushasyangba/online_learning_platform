from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("detail_course/",detail_course,name="detail_course"),
]
