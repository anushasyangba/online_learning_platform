from django.shortcuts import render,get_object_or_404
from .models import Course

# Create your views here.
def show(request):
    return render(request,'index.html')

def class_detail(request):
    course = get_object_or_404(Course)
    return render(request,'class_detail.html',{'course':course})