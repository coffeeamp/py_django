from django.shortcuts import render
from . import models

# Create your views here.

def list_patients(request):
    all_patients = models.Patient.objects.all()
    context_list = {'patients': all_patients} # context_list라는 이름으로 all_patients를 넘겨줌
    
    return render(request, 'my_app/list.html', context=context_list)

def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    
    
    
    return render(request, 'my_app/variable.html',)

