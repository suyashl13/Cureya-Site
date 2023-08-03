from django.db import models
import uuid


# Create your models here.
class PatientAppointment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    patient_name = models.CharField(max_length=50)

    patient_email = models.EmailField(max_length=150)
    patient_mobile = models.CharField(max_length=12)

    doctor = models.CharField(max_length=50)

    patient_problem = models.TextField(max_length=210)

    selected_datetime = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name
