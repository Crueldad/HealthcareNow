from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.

class Healthcare_Categories(models.Model):
    UserID = models.IntegerField(blank=True, primary_key=True)
    UserName = models.CharField(max_length=50, blank=True)
    UserEmail = models.CharField(max_length=50, blank=True)
    UserPassword = models.CharField(max_length=50, blank=True)
    SpecialistServices = models.IntegerField(blank=True)
    PreventativeCare = models.IntegerField(blank=True)
    DiagnosticTest = models.IntegerField(blank=True)
    GenericDrugs = models.IntegerField(blank=True)
    OutpatientSurgery = models.IntegerField(blank=True)
    ImmediateMedicalAttention = models.IntegerField(blank=True)
    OutpatientInpatient = models.IntegerField(blank=True)
    Pregnancy = models.IntegerField(blank=True)
    HomeHealthCare = models.IntegerField(blank=True)
    RehabilationServices = models.IntegerField(blank=True)
    SkilledNursingCare = models.IntegerField(blank=True)
    formSubmissions = models.ForeignKey('questions', on_delete=models.DO_NOTHING)

class questions(models.Model):
    Gender = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Prefer not to say")

    )

    Age = (
    ("4", "18-24"),
    ("5", "25-34"),
    ("6", "35-44"),
    ("7", "45-54")
    )


    Are_you_currently_taking_pescribed_medication = (
    ("8", "Yes"),
    ("9", "No")
    )

    Do_you_receive_regular_physicals_and_health_screenings = (
    ("10", "Yes"),
    ("11", "No")
    )

    Do_you_get_routine_vaccines_or_flu_shots = (
    ("12", "Yes"),
    ("13", "No")
    )

    Do_you_often_use_preventative_services = (
    ("14", "Yes"),
    ("15", "No")
    )

    Do_you_need_prenatal_maternity_services = (
    ("16", "Yes"),
    ("17", "No")
    )

    Do_you_need_OBGYN_services = (
    ("18", "Yes"),
    ("19", "No")
    )

    Do_you_want_to_keep_your_current_doctor = (
    ("20", "Yes"),
    ("21", "No")
    )

    Do_you_need_to_see_various_specialists = (
    ("22", "Yes"),
    ("23", "No")
    )

    Is_emergency_care_or_hospital_care_a_priority = (
    ("24", "Yes"),
    ("25", "No")
    )

    Are_you_diagnosed_with_heart_disease = (
    ("26", "Yes"),
    ("27", "No")
    )

    Are_you_diagnosed_with_cancer = (
    ("28", "Yes"),
    ("29", "No")
    )

    Are_you_pregnant = (
    ("30", "Yes"),
    ("31", "No")
    )

    Are_you_diabetic = (
    ("32", "Yes"),
    ("33", "No")
    )

    Do_you_need_help_with_substance_abuse = (
    ("34", "Yes"),
    ("35", "No")
    )

    Do_you_need_treatement_for_HIV_or_Aids = (
    ("36", "Yes"),
    ("37", "No")
    )

    Do_you_need_treatment_for_depression = (
    ("38", "Yes"),
    ("39", "No")
    )

    Do_you_need_treatment_for_anxiety = (
    ("40", "Yes"),
    ("41", "No")
    )

    Do_you_need_help_with_other_mental_health_disorders = (
    ("42", "Yes"),
    ("43", "No")
    )

    Are_you_a_candidate_for_cataract_surgery = (
    ("44", "Yes"),
    ("45", "No")
    )

    Are_you_a_candidate_for_knee_replacement = (
    ("46", "Yes"),
    ("47", "No")
    )

    Are_you_a_candidate_for_hip_replacement = (
    ("48", "Yes"),
    ("49", "No")
    )

    Gender = models.CharField(max_length=500, blank=True, choices=Gender)
    Age = models.CharField(max_length=500, blank=True, choices=Age)
    Are_you_currently_taking_pescribed_medication = models.CharField(max_length=500, blank=True, choices=Are_you_currently_taking_pescribed_medication)
    Do_you_receive_regular_physicals_and_health_screenings = models.CharField(max_length=500, blank=True, choices=Do_you_receive_regular_physicals_and_health_screenings)
    Do_you_get_routine_vaccines_or_flu_shots = models.CharField(max_length=500, blank=True, choices=Do_you_get_routine_vaccines_or_flu_shots)
    Do_you_often_use_preventative_services = models.CharField(max_length=500, blank=True, choices=Do_you_often_use_preventative_services )
    Do_you_need_prenatal_maternity_services = models.CharField(max_length=500, blank=True, choices=Do_you_need_prenatal_maternity_services)
    Do_you_need_OBGYN_services = models.CharField(max_length=500, blank=True, choices=Do_you_need_OBGYN_services)
    Do_you_want_to_keep_your_current_doctor = models.CharField(max_length=500, blank=True, choices=Do_you_want_to_keep_your_current_doctor )
    Do_you_need_to_see_various_specialists = models.CharField(max_length=500, blank=True, choices= Do_you_need_to_see_various_specialists)
    Is_emergency_care_or_hospital_care_a_priority = models.CharField(max_length=500, blank=True, choices=Is_emergency_care_or_hospital_care_a_priority)
    Are_you_diagnosed_with_heart_disease = models.CharField(max_length=500, blank=True, choices=Are_you_diagnosed_with_heart_disease)
    Are_you_diagnosed_with_cancer = models.CharField(max_length=500, blank=True, choices=Are_you_diagnosed_with_cancer )
    Are_you_pregnant = models.CharField(max_length=500, blank=True, choices=Are_you_pregnant)
    Are_you_diabetic = models.CharField(max_length=500, blank=True, choices=Are_you_diabetic)
    Do_you_need_help_with_substance_abuse = models.CharField(max_length=500, blank=True, choices=Do_you_need_help_with_substance_abuse)
    Do_you_need_treatement_for_HIV_or_Aids = models.CharField(max_length=500, blank=True, choices=Do_you_need_treatement_for_HIV_or_Aids)
    Do_you_need_treatment_for_depression = models.CharField(max_length=500, blank=True, choices=Do_you_need_treatment_for_depression)
    Do_you_need_treatment_for_anxiety = models.CharField(max_length=500, blank=True, choices=Do_you_need_treatment_for_anxiety)
    Do_you_need_help_with_other_mental_health_disorders = models.CharField(max_length=500, blank=True, choices=Do_you_need_help_with_other_mental_health_disorders)
    Are_you_a_candidate_for_cataract_surgery = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_cataract_surgery)
    Are_you_a_candidate_for_knee_replacement = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_knee_replacement)
    Are_you_a_candidate_for_hip_replacement = models.CharField(max_length=500, blank=True, choices=Are_you_a_candidate_for_hip_replacement)
