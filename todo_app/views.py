from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is the todo app homepage.')

def detail(request):
    return HttpResponse('This is the detail page of todo application')