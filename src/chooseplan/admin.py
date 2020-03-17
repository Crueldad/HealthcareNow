from django.contrib import admin

# Register your models here.
from .models import demographics 
from .models import Symptoms


admin.site.register(demographics)
admin.site.register(Symptoms)
