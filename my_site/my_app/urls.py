from django.urls import path, include
from . import views


app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('rental_review/', views.rental_review, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('classroom/',include('classroom.urls')),
]