from django import forms
from .models import questions
from django.forms import ModelForm
from multiselectfield import MultiSelectField

class chooseplanform(forms.ModelForm):
    class Meta:
        model = questions
        fields = '__all__'
        widgets = {'Gender': forms.CheckboxSelectMultiple, 'Age': forms.CheckboxSelectMultiple, 'Are_you_currently_taking_pescribed_medication': forms.CheckboxSelectMultiple, 'Which_services_are_most_important_for_you_in_a_health_plan': forms.CheckboxSelectMultiple, 'Select_all_conditions_you_have_been_diagnosed_with': forms.CheckboxSelectMultiple, 'Has_a_doctor_notified_you_as_a_candidate_for': forms.CheckboxSelectMultiple}










    # SpecialistServices = forms.IntegerField()
    # PreventativeCare = forms.IntegerField()
    # DiagnosticTest = forms.IntegerField()
    # GenericDrugs = forms.IntegerField()
    # OutpatientSurgery = forms.IntegerField()
    # ImmediateMedicalAttention = forms.IntegerField()
    # OutpatientInpatient = forms.IntegerField()
    # Pregnancy = forms.IntegerField()
    # HomeHealthCare = forms.IntegerField()
    # RehabilationServices = forms.IntegerField()
    # SkilledNursingCare = forms.IntegerField()
