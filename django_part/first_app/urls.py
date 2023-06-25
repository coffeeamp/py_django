from django.urls import path
from . import views


# first_app/

urlpatterns = [
    path('<topic>', views.news_view, name='news') # 토픽을 받아서 뉴스뷰로 넘겨줌
]
