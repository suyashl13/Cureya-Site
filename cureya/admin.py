from django.contrib import admin
from .models import PatientAppointment, Message, TeamMember, Section, Content

# Register your models here.
admin.site.register(PatientAppointment)
admin.site.register(Message)
admin.site.register(TeamMember)
admin.site.register(Section)
admin.site.register(Content)
