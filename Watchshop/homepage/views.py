from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return HttpResponse("Hello Django")

# Create your views here.