from django.shortcuts import render
from datetime import datetime


def home(request):

    now = datetime.now()
    # 일단은 고정이미지
    background = "https://user-images.githubusercontent.com/96712990/177008848-2d8d7b00-79d1-4cc9-9fe7-d0095047bb2d.jpg"
    context = {
        'current_date': now,
        'background': background
    }
    return render(request, 'main/home.html', context)


def navbar(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'include/navbar.html', context)
