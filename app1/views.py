from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hai(request):
    return HttpResponse('rohit')
def hello(request):
    return HttpResponse('chiku')   