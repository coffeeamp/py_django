from django.contrib import admin
from .models import Car, Review, Quiz, Student
# Register your models here.
admin.site.register(Review)


class CarAdmin(admin.ModelAdmin):
    fieldsets = [ # 필드셋을 이용하여 필드를 그룹화, 각 그룹의 이름을 지정
        ('TIME INFORMATION', {'fields': ['year']}), # 필드셋의 이름은 튜플의 첫 번째 요소, 두 번째 요소는 딕셔너리, 딕셔너리의 키는 필드 이름, 값은 필드 이름의 리스트
        ('CAR INFORMATION', {'fields': ['brand']}),
    ]
admin.site.register(Car,CarAdmin)
admin.site.register(Quiz)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','student_name', 'email']
