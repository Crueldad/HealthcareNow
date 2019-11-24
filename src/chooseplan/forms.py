from django import forms
from .models import questions
from django.forms import ModelForm

class chooseplanform(forms.ModelForm):
    class Meta:
        model = questions
        fields = '__all__'
        widgets = {'Gender': forms.RadioSelect, 'Age': forms.RadioSelect, 'Are_you_currently_taking_pescribed_medication': forms.RadioSelect,  'Do_you_receive_regular_physicals_and_health_screenings': forms.RadioSelect, 'Do_you_often_come_in_for_routine_checkups': forms.RadioSelect, \
        'Do_you_need_prenatal_maternity_services': forms.RadioSelect, 'Do_you_need_treatement_for_HIV_or_Aids': forms.RadioSelect, 'Do_you_often_deal_with_skin_conditions': forms.RadioSelect, 'Do_you_often_participate_in_sports': forms.RadioSelect, 'Are_you_diagnosed_with_heart_disease': forms.RadioSelect, 'Are_you_diagnosed_with_cancer': forms.RadioSelect, \
        'Are_you_pregnant': forms.RadioSelect, 'Are_you_diabetic': forms.RadioSelect, 'Do_you_need_help_with_substance_abuse': forms.RadioSelect, 'Do_you_have_a_labor_intensive_job': forms.RadioSelect, 'Do_you_often_feel_chronic_pain': forms.RadioSelect, 'Are_you_diagnosed_with_a_mental_health_condition': forms.RadioSelect, \
        'Do_you_need_help_with_other_mental_health_disorders': forms.RadioSelect, 'Are_you_a_candidate_for_cataract_surgery': forms.RadioSelect, 'Are_you_a_candidate_for_knee_replacement': forms.RadioSelect, 'Are_you_a_candidate_for_hip_replacement': forms.RadioSelect,
        'Do_you_come_in_for_annual_mammogram_or_prostate_exams': forms.RadioSelect, 'Are_you_a_candidate_for_cataract_surgery ': forms.RadioSelect, 'Are_you_a_candidate_for_knee_replacement': forms.RadioSelect, 'Are_you_a_candidate_for_hip_replacement': forms.RadioSelect, 'Do_you_get_routine_vaccines_or_flu_shots': forms.RadioSelect}

