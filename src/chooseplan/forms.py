from django import forms

class chooseplanform(forms.Form):
    SpecialistServices = forms.IntegerField()
    PreventativeCare = forms.IntegerField()
    DiagnosticTest = forms.IntegerField()
    GenericDrugs = forms.IntegerField()
    OutpatientSurgery = forms.IntegerField()
    ImmediateMedicalAttention = forms.IntegerField()
    OutpatientInpatient = forms.IntegerField()
    Pregnancy = forms.IntegerField()
    HomeHealthCare = forms.IntegerField()
    RehabilationServices = forms.IntegerField()
    SkilledNursingCare = forms.IntegerField()
