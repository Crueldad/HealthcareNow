from django.db import models


class HealthPlan(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
