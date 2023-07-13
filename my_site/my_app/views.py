from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm
from django.views.generic import TemplateView, FormView
from my_app.forms import ContactForm

# Create your views here.

# def list_patients(request):
#     all_patients = models.Patient.objects.all()
#     context_list = {'patients': all_patients} # context_list라는 이름으로 all_patients를 넘겨줌
    
#     return render(request, 'my_app/list.html', context=context_list)

def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    return render(request, 'my_app/variable.html',)

#----------------------------------------------# 
# 2023.07.07
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'my_app/list.html', context=context)

def add(request):
    if request.POST: # POST 방식으로 요청이 들어왔을 때
        brand = request.POST['brand'] # 브랜드 이름을 받아옴
        year = int(request.POST['year']) # 년도를 받아옴
        models.Car.objects.create(brand=brand, year=year) # DB에 저장
        # 사용자가 새 차량을 추가하면 list.html로 redirect
        return redirect(reverse('my_app:list')) # list.html로 redirect
    else:    
        return render(request, 'my_app/add.html')

def delete(request):
    if request.POST:
        # delete the car
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('my_app:list'))
        except:
            print('삭제할 차량이 없습니다.')
    else:
        return render(request, 'my_app/delete.html')

#----------------------------------------------#
# 2023.07.10

def rental_review(request):
    # POST REQUEST -> FORM CONTENTS -> THANK YOU
    if request.method == 'POST':
        form = ReviewForm(request.POST) # form에 POST 요청의 내용을 담음
        if form.is_valid(): # form이 유효하다면
            form.save() # form을 저장
            # {'name': '이름', 'email': '이메일', 'review': '후기'}
            print(form.cleaned_data) # form.cleaned_data를 출력
            return redirect(reverse('my_app:thank_you')) # thank_you.html로 redirect
        
    # ELSE, RENDER FORM
    else: # GET 요청이 들어왔을 때
        form = ReviewForm() # form에 ReviewForm을 담음
    return render(request, 'my_app/rental_review.html',context={'form':form})

def thank_you(request):
    return render(request, 'my_app/thank_you.html')

#----------------------------------------------#
# 2023.07.13

class HomeView(TemplateView):
    template_name = 'my_app/home.html'

class ContactFormView(FormView):
    form_class = ContactForm
