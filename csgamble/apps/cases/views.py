from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>CASES</h1>')

def case(request, case_name):
    return HttpResponse(f'<h1>SPECIFIC CASE - {case_name}</h1>')