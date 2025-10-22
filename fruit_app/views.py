from django.shortcuts import render
from django.http import JsonResponse
import json
from .fruits_data import fruits

# Create your views here.


def send_fruites(request):
    for fruit in fruits:
        result = fruit
    return JsonResponse(result)
