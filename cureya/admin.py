from django.contrib import admin
from .models import PatientAppointment, Message, TeamMember, Section, Content, PublishBookResponse, DoctorListingEnquiry, DiagnosticListingEnquiry

# Register your models here.
admin.site.register(PatientAppointment)
admin.site.register(Message)
admin.site.register(TeamMember)
admin.site.register(Section)
admin.site.register(Content)
admin.site.register(PublishBookResponse)
admin.site.register(DoctorListingEnquiry)
admin.site.register(DiagnosticListingEnquiry)
