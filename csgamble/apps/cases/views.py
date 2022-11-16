from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Case


def index(request):
    return HttpResponse('<h1>CASES</h1>')


def case(request, case_name):
    case = get_object_or_404(Case, name=case_name)
    context = {
        'case': case
    }
    return render(request, 'cases/case.html', context)
