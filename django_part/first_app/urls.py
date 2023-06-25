from django.urls import path
from . import views


# first_app/

urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view), # 토픽을 받아서 뉴스뷰로 넘겨줌
]
