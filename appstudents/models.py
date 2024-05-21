from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 150)
    course = models.CharField(max_length= 170, default= "Software Engineering 3")

    def __str__(self):
        return self.name
