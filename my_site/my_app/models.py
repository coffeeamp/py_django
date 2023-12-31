from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()  # 사람 나이는 정수로 표현
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."
    
    
#----------------------------------------------#

class Car(models.Model):
    #pk
    brand = models.CharField(max_length=30) # 차 브랜드는 문자열로 표현 최대 30자
    year = models.IntegerField() # 차 연식은 정수로 표현
    
    def __str__(self): # 객체를 문자열로 표현할 때 사용
        return f"Car is {self.brand} {self.year}"   # Car is brand year


class Review(models.Model):
    name = models.CharField(max_length=30)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # 별점은 1~5 사이의 정수
    
    

#----------------------------------------------#
# API 테스트용 모델
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    subject = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and teaches {self.subject}."
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
#----------------------------------------------#
# Flutter Contact Test
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

#----------------------------------------------#
# Post Test
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
#----------------------------------------------#
# todo Test
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
