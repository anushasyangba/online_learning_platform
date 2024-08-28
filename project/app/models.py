from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

# Create your models here.
# class Product(models.Model):
#     image=models.ImageField(upload_to='prodcuts',null=True,blank=True) 
#     name=models.CharField(max_length=50)
#     desc=models.CharField(max_length=200)
#     rating=models.PositiveIntegerField()
        
#     def __str__(self) -> str:
#         return self.name 

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    includes = models.JSONField(default=list)  # ['Syllabus', 'Videos', 'Quizzes', ...]

    def __str__(self):
        return self.title