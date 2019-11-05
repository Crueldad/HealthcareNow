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
