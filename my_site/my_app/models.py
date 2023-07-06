from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()  # 사람 나이는 정수로 표현
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."
