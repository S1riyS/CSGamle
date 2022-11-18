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

    print(case.caseitem_set.all())
    for i in case.caseitem_set.all():
        print(i.wear_level)

    return render(request, 'cases/case.html', context)
