from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello Django')


def product(request):
    responce  = '<h1>Product № 1</h1>'
    responce += '<h1>Product № 2</h1>'
    responce += '<h1>Product № 3</h1>'
    responce += '<h1>Product № 4</h1>'
    responce += '<h1>Product № 5</h1>'
    responce += '<h1>Product № 6</h1>'
    responce += '<h1>Product № 7</h1>'
    return HttpResponse(responce)