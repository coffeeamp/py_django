from django.shortcuts import render
from django.http import HttpResponse



articles = {
    'sports' : 'Spors page',
    'finance' : 'Finance page',
    'politics' : 'Politics page',
}

def news_view(request, topic):
    return HttpResponse(articles[topic])

