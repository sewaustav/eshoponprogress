from django.http import HttpResponse
from django.shortcuts import render, redirect

def main(request):
    data = {
        'title': 'Главная страница',
        'head': 'Заголовок',
        'text': 'Добро пожаловать!!!',
    }
    return render(request, 'shop/main.html', data)