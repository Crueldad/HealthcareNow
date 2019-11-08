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

class questions(models.Model):
    Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say")

    )

    Age = (
    ("18-24", "18-24"),
    ("25-34", "25-34"),
    ("35-44", "35-44"),
    ("45-54", "45-54")
    )


    Are_you_currently_taking_pescribed_medication = (
    ("Yes", "Yes"),
    ("No", "No")
    )

    Which_services_are_most_important_for_you_in_a_health_plan = (
    ("Regular physicals and health screenings", "Regular physicals and health screenings"),
    ("Prescription drug coverage (brand name and/or generic)", "Prescription drug coverage (brand name and/or generic)"),
    ("Get routine vaccines or flu shots?", "Get routine vaccines or flu shots?"),
    ("Preventative services", "Preventative services"),
    ("Prenatal/Maternity services", "Prenatal/Maternity services"),
    ("OB-GYN", "OB-GYN"),
    ("Keeping your doctor", "Keeping your doctor"),
    ("Use of specialists", "Use of specialists"),
    ("Emergency and hospital care", "Emergency and hospital care")
    )

    Select_all_conditions_you_have_been_diagnosed_with = (
    ("Heart Disease (Cardiovascular Disease)", "Heart Disease (Cardiovascular Disease)"),
    ("Cancer", "Cancer"),
    ("Pregnancy", "Pregnancy"),
    ("Diabetes (Type 1, Type 2, or Gestational)", "Diabetes (Type 1, Type 2, or Gestational)"),
    ("Substance absue issues (drugs (illicit or prescription) and/or alcohol)", "Substance absue issues (drugs (illicit or prescription) and/or alcohol)"),
    ("HIV/AIDS", "HIV/AIDS"),
    ("Depression", "Depression"),
    ("Anxiety", "Anxiety"),
    ("Other mental health disorders (may include but not limited to: Bipolar Disorder, Attention-Deficit/Hyperactivity Disorder (ADD or ADHD), Schizophrenia, Autism, Borderline personality disorder (BPD), Dissociative Disorders, Eating Disorders, Posttraumatic Stress Disorder (PTSD)))", "Other mental health disorders (may include but not limited to: Bipolar Disorder, Attention-Deficit/Hyperactivity Disorder (ADD or ADHD), Schizophrenia, Autism, Borderline personality disorder (BPD), Dissociative Disorders, Eating Disorders, Posttraumatic Stress Disorder (PTSD)))")
    )

    Has_a_doctor_notified_you_as_a_candidate_for = (
    ("Cataract Surgery", "Cataract Surgery"),
    ("Knee Replacement", "Knee Replacement"),
    ("Hip Replacement", "Hip Replacement")
    )

    Gender = models.CharField(max_length=500, blank=True, choices=Gender)
    Age = models.CharField(max_length=500, blank=True, choices=Age)
    Are_you_currently_taking_pescribed_medication = models.CharField(max_length=500, blank=True, choices=Are_you_currently_taking_pescribed_medication)
    Which_services_are_most_important_for_you_in_a_health_plan = models.CharField(max_length=500, blank=True, choices=Which_services_are_most_important_for_you_in_a_health_plan)
    Select_all_conditions_you_have_been_diagnosed_with = models.CharField(max_length=500, blank=True, choices=Select_all_conditions_you_have_been_diagnosed_with)
    Has_a_doctor_notified_you_as_a_candidate_for = models.CharField(max_length=500, blank=True, choices=Has_a_doctor_notified_you_as_a_candidate_for)












    # male = models.CharField(max_length=50, blank=True)
    # female = models.CharField(max_length=50, blank=True)
    # prefernottosay = models.CharField(max_length=50, blank=True)
    # a18to21 = models.CharField(max_length=50, blank=True)
    # a25to34 = models.CharField(max_length=50, blank=True)
    # a35to44 = models.CharField(max_length=50, blank=True)
    # a45to54 = models.CharField(max_length=50, blank=True)
    # pyes = models.CharField(max_length=50, blank=True)
    # pno = models.CharField(max_length=50, blank=True)
    # rphs = models.CharField(max_length=50, blank=True)
    # pgc = models.CharField(max_length=50, blank=True)
    # vacineflu = models.CharField(max_length=50, blank=True)
    # prevs = models.CharField(max_length=50, blank=True)
    # prenatal = models.CharField(max_length=50, blank=True)
    # obgyn = models.CharField(max_length=50, blank=True)
    # keepdoctor = models.CharField(max_length=50, blank=True)
    # usespecialist = models.CharField(max_length=50, blank=True)
    # emergency = models.CharField(max_length=50, blank=True)
    # hd = models.CharField(max_length=50, blank=True)
    # cancer = models.CharField(max_length=50, blank=True)
    # preg = models.CharField(max_length=50, blank=True)
    # diabetes = models.CharField(max_length=50, blank=True)
    # substance = models.CharField(max_length=50, blank=True)
    # hiv = models.CharField(max_length=50, blank=True)
    # depression = models.CharField(max_length=50, blank=True)
    # anxiety = models.CharField(max_length=50, blank=True)
    # other = models.CharField(max_length=50, blank=True)
