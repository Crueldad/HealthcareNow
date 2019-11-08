from django.contrib import admin

# Register your models here.
from .models import Healthcare_Categories
from .models import questions

admin.site.register(Healthcare_Categories)
admin.site.register(questions)
