from django.urls import path, include
from . import views
from .views import (HomeView,
                    ContactFormView, 
                    TeacherCreateView,
                    TeacherListView,
                    TeacherDetailView,
                    TeacherUpdateView,
                    TeacherDeleteView,
                    helloAPI, randomQuizAPI, teacherAPI,
                    PostListCreateView,
                    )


app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('rental_review/', views.rental_review, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('detail_teacher/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher'),
    path('hello/', helloAPI),
    path('<int:pk>/', randomQuizAPI),
    path('teacher/', teacherAPI),
    path('student/', views.StudentList.as_view(), name='student'),
    path('post/', PostListCreateView.as_view(), )
]