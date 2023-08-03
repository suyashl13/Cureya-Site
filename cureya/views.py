from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render
from datetime import datetime
from .models import PatientAppointment


# Create your views here.
def home(request: ASGIRequest):
    if request.method == 'POST':
        nw_appointment = PatientAppointment()

        nw_appointment.patient_name = request.POST['patient_name']
        nw_appointment.patient_email = request.POST['email']
        nw_appointment.patient_mobile = request.POST['mobile']
        nw_appointment.doctor = request.POST['doctor']

        nw_appointment.patient_problem = request.POST['problem']

        recieved_datetime = '{} {}'.format(request.POST['date_selected'], request.POST['time_selected'])
        recieved_datetime_fmt = '%m/%d/%Y %I:%M %p'

        nw_appointment.selected_datetime = datetime.strptime(recieved_datetime, recieved_datetime_fmt)

        nw_appointment.save()
        return render(request, 'index.html', {'msg': 'Appointment added successfully'.upper()})

    return render(request, 'index.html', {'msg': None})


def about(request):
    return render(request, 'about.html')
