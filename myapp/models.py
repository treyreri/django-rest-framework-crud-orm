from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name