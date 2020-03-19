from django.contrib import admin

# Register your models here.
from .models import Hospital, Service

class ServiceInLine(admin.TabularInline):
    model = Service
    extra = 3

class HospitalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['hospital_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ServiceInLine]
    list_display = ('question_text', 'pub_date')

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Service)
