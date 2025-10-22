from django.shortcuts import render
from django.http import JsonResponse
import json
from .fruits_data import fruits

# Create your views here.


def send_fruites(request):
    fruits = [
        {"name": "Apple",  "weight": 200, "color": "red"},
        {"name": "Banana", "weight": 120, "color": "yellow"},
        {"name": "Grape",  "weight": 5,   "color": "purple"},
        {"name": "Pear",   "weight": 220, "color": "green"},
        {"name": "Orange", "weight": 250, "color": "orange"},
    ]
    return JsonResponse(fruits, safe=False)
