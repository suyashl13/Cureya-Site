from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render
from datetime import datetime
from .models import PatientAppointment, Message


# Create your views here.
def home(request: ASGIRequest):
    if request.method == 'POST':
        try:
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
        except Exception:
            return render(request, 'index.html', {'msg': 'Appointment Not Added'.upper()})

    return render(request, 'index.html', {'msg': None})


def about(request: ASGIRequest):

    if request.method == 'POST':
        try:
            print(request.POST)
            msg = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], message=request.POST['message'])
            msg.save()

            return render(request, 'about.html', {'msg': 'Message sent successfully!'})
        except Exception as e:
            print(e)

    return render(request, 'about.html', {'msg': None})
