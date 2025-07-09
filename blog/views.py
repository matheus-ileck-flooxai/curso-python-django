from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('BLOG')

    return HttpResponse('BLOG')

def exemplo(request):
    print('exemplo')

    return HttpResponse('exemplo do app 1')