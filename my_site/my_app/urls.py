from django.urls import path
from . import views


app_name = 'my_app'

urlpatterns = [
    # path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete')
]