from django.shortcuts import render
from django.http import HttpResponse
from .forms import chooseplanform
from .models import questions




# def chooseplan(request):
#     return render(request, 'chooseplan/chooseplan.html')

def chooseplan(request):
    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Thank You')
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form})

# def algorithm(request, formsresult):
#     ### insert into DB
