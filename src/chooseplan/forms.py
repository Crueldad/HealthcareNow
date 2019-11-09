from django import forms
from .models import questions
from django.forms import ModelForm
from multiselectfield import MultiSelectField

class chooseplanform(forms.ModelForm):
    class Meta:
        model = questions
        fields = '__all__'
        widgets = {'Gender': forms.RadioSelect, 'Age': forms.RadioSelect, 'Do_you_get_routine_vaccines_or_flu_shots': forms.RadioSelect,  'Do_you_often_use_preventative_services': forms.RadioSelect,  'Do_you_need_prenatal_maternity_services': forms.RadioSelect, \
        'Do_you_need_OBGYN_services': forms.RadioSelect, 'Do_you_want_to_keep_your_current_doctor': forms.RadioSelect, 'Do_you_need_to_see_various_specialists': forms.RadioSelect, 'Is_emergency_care_or_hospital_care_a_priority': forms.RadioSelect, 'Are_you_diagnosed_with_heart_disease': forms.RadioSelect, 'Are_you_diagnosed_with_cancer': forms.RadioSelect, \
        'Are_you_pregnant': forms.RadioSelect, 'Are_you_diabetic': forms.RadioSelect, 'Do_you_need_help_with_substance_abuse': forms.RadioSelect, 'Do_you_need_treatement_for_HIV_or_Aids': forms.RadioSelect, 'Do_you_need_treatment_for_depression': forms.RadioSelect, 'Do_you_need_treatment_for_anxiety': forms.RadioSelect, \
        'Do_you_need_help_with_other_mental_health_disorders': forms.RadioSelect, 'Are_you_a_candidate_for_cataract_surgery': forms.RadioSelect, 'Are_you_a_candidate_for_knee_replacement': forms.RadioSelect, 'Are_you_a_candidate_for_hip_replacement': forms.RadioSelect,
        'Are_you_currently_taking_pescribed_medication': forms.RadioSelect, 'Do_you_receive_regular_physicals_and_health_screenings': forms.RadioSelect}










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
