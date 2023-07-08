from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()  # 사람 나이는 정수로 표현
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."
    
    
#----------------------------------------------#
# 2023.07.07

class Car(models.Model):
    #pk
    brand = models.CharField(max_length=30) # 차 브랜드는 문자열로 표현 최대 30자
    year = models.IntegerField() # 차 연식은 정수로 표현
    
    def __str__(self): # 객체를 문자열로 표현할 때 사용
        return f"Car is {self.brand} {self.year}"   # Car is brand year
