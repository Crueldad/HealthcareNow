from django.shortcuts import render
from django.http import HttpResponse
from .forms import chooseplanform


# def chooseplan(request):
#     return render(request, 'chooseplan/chooseplan.html')

def chooseplan(request):
    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            Gender = form.cleaned_data.get('Gender')
            Age = form.cleaned_data.get('Age')
            Are_you_currently_taking_prescription_medication = form.cleaned_data.get('Are_you_currently_taking_prescription_medication')
            When_searching_for_a_health_plan_which_services_are_most_important_for_you = form.cleaned_data.get('When_searching_for_a_health_plan_which_services_are_most_important_for_you')
            Have_you_been_diagnosed_by_a_doctor_for_any_of_the_following_conditions_Check_all_that_may_apply = form.cleaned_data.get('Have_you_been_diagnosed_by_a_doctor_for_any_of_the_following_conditions_Check_all_that_may_apply')
            # return HttpResponse('Thank You')
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form})

# def algorithm(request, formsresult):
#     ### insert into DB
