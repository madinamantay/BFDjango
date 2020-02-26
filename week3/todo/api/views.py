from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    print(request)
    return HttpResponse('asd')
