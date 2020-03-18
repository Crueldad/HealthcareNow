from django.http import HttpResponse
from django.shortcuts import render, redirect

from chooseplan.forms import chooseplanform

def index(request):
    return render(request, 'algorithm/results.html')
