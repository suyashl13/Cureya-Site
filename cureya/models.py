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


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=220)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.message)


class TeamMember(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=60)
    experience_years = models.IntegerField(default=0)

    photo = models.ImageField(upload_to='team/')
    designation = models.CharField(max_length=40)

    priority = models.IntegerField(default=3)

    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.designation)


class Section(models.Model):
    CONTENT_CHOICES = (
        ('P', 'Paragraph'),
        ('B', 'Bullet')
    )
    SECTION_SIZE_CHOICES = (
        ('SM', 'SMALL'),
        ('LG', 'LARGE')
    )

    section_name = models.CharField(max_length=60, default='')
    team_mate = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null=True)

    section_size = models.CharField(max_length=2, choices=SECTION_SIZE_CHOICES, default='P')
    content_type = models.CharField(max_length=1, choices=CONTENT_CHOICES, default='LG')

    def __str__(self):
        return '{} - {}'.format(self.team_mate.name, self.section_name)


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    content = models.TextField(max_length=555)

    def __str__(self):
        return '{} ({})'.format(self.section.section_name, self.section.team_mate.name)


class PublishBookResponse(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=110)
    phone = models.CharField(max_length=14)

    publish_information = models.TextField(
        max_length=255
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)