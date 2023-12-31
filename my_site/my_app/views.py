from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from . import models
from my_app.models import Teacher
from .forms import ReviewForm
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
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

# TemplateView
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

# FormView
class HomeView(TemplateView):
    template_name = 'my_app/home.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'my_app/contact.html'
    
    # success_url
    success_url = '/my_app/thank_you/'
    
    # form_valid
    def form_valid(self, form):
        print(form.cleaned_data)
        # 함수기반뷰의 ContactForm(request.POST) -> 클래스기반뷰 form.cleaned_data
        return super().form_valid(form)

# CreateView
class TeacherCreateView(CreateView):
    model = Teacher # 1단계 모델에 연결
    fields = "__all__" # 2단계 필드에 연결, 모든 필드가 이 템플릿에 표시되도록 __all__을 사용
    success_url = reverse_lazy('my_app:thank_you') # 3단계 성공하면 thank_you.html로 이동
    
# ListView
class TeacherListView(ListView):
    # model_list.html 템플릿에 연결
    model = Teacher
    
    # 디폴트 쿼리 재정의
    queryset = Teacher.objects.order_by('age')
    
    # model_list.html 템플릿에 넘겨줄 context_object_name 설정
    context_object_name = 'teachers_list' # context_object_name을 teachers로 설정
    


# DetailView
class TeacherDetailView(DetailView):
    # model_detail.html 템플릿에 연결
    model = Teacher
    
    # PK --> {{teacher}} /DetailView의 역할은 Teacher의 특정 PK에 대한 teacher를 이 html에 대한 context 객체로 보내는것
class TeacherUpdateView(UpdateView):
    # model_form.html 템플릿에 연결
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('my_app:list_teacher')
class TeacherDeleteView(DeleteView):
    # Form -> form_confirm_delete.html 템플릿에 연결
    # default template_name = my_app/teacher_confirm_delete.html
    
    model = Teacher
    success_url = reverse_lazy('my_app:list_teacher')

#--------------------------------#
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuizSerializer, TeacherSerializer
from .models import Quiz
import random


@api_view(['GET']) # GET 요청만 받음
def helloAPI(request): # API테스트를 위한 샘플 코드
    return Response("hello world!")

# 퀴즈 목록을 보여주는 API
@api_view(['GET'])
def randomQuizAPI(request,id): # id를 받아와서 id개수만큼 랜덤으로 퀴즈를 뽑아서 보여줌
    totalQuizs = Quiz.objects.all() # 모든 퀴즈를 가져옴
    randomQuizs = (list(totalQuizs) ) # totalQuizs를 list로 만들고 id개수만큼 랜덤으로 뽑음
    serializer = QuizSerializer(randomQuizs, many=True) #many 부분을 통해 다량의 데이터도 직렬화 진행
    return Response(serializer.data)

@api_view(['GET'])
def teacherAPI(request):
    teachers = Teacher.objects.all() # name과 age만 가져옴
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

#--------------------------------#
# flutter와 연동하기 위한 API
from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework import permissions
class StudentList(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#--------------------------------#
# Post API
from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#--------------------------------#
# Todo API
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
