from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse(json.dumps({'token': 'ok'}))
    return HttpResponseNotAllowed('Only GET request are allowed')
# Create your views here.

def add_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.body:
            data = json.loads(request.body)
            result = data['A'] + data['B']
            try:
                result_int = int(result)
                print(result_int)

            except ValueError:
                print({"error": "Division by zero!"})
            print(data)
        return JsonResponse({'answer': result})


def subtract_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.body:
            data = json.loads(request.body)
            result = data['A'] - data['B']
            try:
                result_int = int(result)
                print(result_int)

            except ValueError:
                print({"error": "Division by zero!"})
            print(data)
        return JsonResponse({'answer': result})


def multiply_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.body:
            data = json.loads(request.body)
            result = data['A'] * data['B']
            try:
                result_int = int(result)
                print(result_int)

            except ValueError:
                print({"error": "Division by zero!"})
            print(data)
        return JsonResponse({'answer': result})


def divide_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.body:
            data = json.loads(request.body)
            result = data['A'] / data['B']
            try:
                result_int = int(result)
                print(result_int)

            except ValueError:
                print({"error": "Division by zero!"})
            print(data)
        return JsonResponse({'answer': result})
