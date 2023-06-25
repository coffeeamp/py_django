from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect



articles = {  
    'sports' : 'Spors page',
    'finance' : 'Finance page',
    'politics' : 'Politics page',
}

def news_view(request, topic):
    
    ## 예외처리방법
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("Page not found") # 404 에러를 발생시킴
        
def num_page_view(request, num_page):
    
    topics_list = list(articles.keys()) # [sports, finance, politics] 인덱스는 0,1,2
    topic = topics_list[num_page] # 0,1,2 중 하나의 값을 가짐
    
    return HttpResponseRedirect(topic)

# #동적 라우팅,뷰
# def add_view(request, num1, num2):
#     # domain.com/first_app/3/4 --> 7
#     add_result = num1 + num2
#     result = f"{num1} + {num2} = {add_result}"
#     return HttpResponse(str(result))
