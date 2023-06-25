from django.urls import path
from . import views


# first_app/
urlpatterns = [
    path('<topic>', views.news_view, name='news')
]
