from django.shortcuts import render
from django.http import HttpResponse
from .forms import chooseplanform


def chooseplan(request):
    return render(request, 'chooseplan/chooseplan.html')

def get(request):
    form = chooseplanform()
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponse('Thank You')
    return render(request, 'chooseplan/chooseplan.html', {'chooseplanform': form})
