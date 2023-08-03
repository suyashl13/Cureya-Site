from django.contrib import admin
from .models import PatientAppointment, Message

# Register your models here.
admin.site.register(PatientAppointment)
admin.site.register(Message)