from django.shortcuts import render
from django.http import HttpResponse
from chooseplan.forms import chooseplanform


def chooseplan(request):
    return render(request, 'chooseplan/chooseplan.html')

def get(self, request):
    form = chooseplanform()
    return render(request, self.chooseplan.html, {'form': form})
