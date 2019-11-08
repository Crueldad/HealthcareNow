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
            Gender = form.cleaned_data.get('Gender')
            Age = form.cleaned_data.get('Age')
            Are_you_currently_taking_pescribed_medication = form.cleaned_data.get('Are_you_currently_taking_pescribed_medication')
            Which_services_are_most_important_for_you_in_a_health_plan = form.cleaned_data.get('Which_services_are_most_important_for_you_in_a_health_plan')
            Select_all_conditions_you_have_been_diagnosed_with = form.cleaned_data.get('Select_all_conditions_you_have_been_diagnosed_with')
            Has_a_doctor_notified_you_as_a_candidate_for = form.cleaned_data.get('Has_a_doctor_notified_you_as_a_candidate_for')
            form.save()
            # return HttpResponse('Thank You')
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form})

# def algorithm(request, formsresult):
#     ### insert into DB
