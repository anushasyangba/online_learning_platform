from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def detail_course(request):
    return render(request,'detail_course.html')