from django import forms

class chooseplanform(forms.Form):
    OPTIONS = (
        ("M", "Male"),
        ("F", "Female"),
        ("PNTS", "Prefer not to say")
    )
    Gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    Age = (
        ("18-24", "18-24"),
        ("25-34", "25-34"),
        ("35-44", "35-44"),
        ("45-54", "45-54")
    )
    Age = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Age)

    Are_you_currently_taking_prescription_medication = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    Are_you_currently_taking_prescription_medication = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Are_you_currently_taking_prescription_medication)

    When_searching_for_a_health_plan_which_services_are_most_important_for_you = (
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
    When_searching_for_a_health_plan_which_services_are_most_important_for_you = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=When_searching_for_a_health_plan_which_services_are_most_important_for_you)

    Have_you_been_diagnosed_by_a_doctor_for_any_of_the_following_conditions_Check_all_that_may_apply = (
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
    Have_you_been_diagnosed_by_a_doctor_for_any_of_the_following_conditions_Check_all_that_may_apply = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Have_you_been_diagnosed_by_a_doctor_for_any_of_the_following_conditions_Check_all_that_may_apply)







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
