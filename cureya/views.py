from uuid import UUID

from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render, redirect
from datetime import datetime
from .models import PatientAppointment, Message, TeamMember, Section, Content, PublishBookResponse, \
    DiagnosticListingEnquiry, DoctorListingEnquiry


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
            msg = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                          message=request.POST['message'])
            msg.save()

            return render(request, 'about.html', {'msg': 'Message sent successfully!'})
        except Exception as e:
            print(e)

    return render(request, 'about.html', {'msg': None})


def service(request: ASGIRequest):
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

            return render(request, 'service.html', {'msg': 'Appointment added successfully'.upper()})
        except Exception:
            return render(request, 'service.html', {'msg': 'Appointment Not Added'.upper()})
    return render(request, 'service.html')


def team(request: ASGIRequest):
    team_members = TeamMember.objects.filter(is_visible=True).order_by('-priority', '-experience_years')
    return render(request, 'team.html', {'team': team_members})


def team_slug(request: ASGIRequest, id):
    context = {}

    try:
        member = TeamMember.objects.get(pk=UUID(id))
        sections = Section.objects.filter(team_mate=id)
        data = []
        for section in list(sections.values()):
            section['content'] = list(
                (Content.objects.filter(section=section['id'])).values()
            )
            data.append(section)

        context['team_member'] = member
        context['sections'] = data

        return render(request, 'team-slug.html', context)
    except Exception:
        return render(request, '404.html')


def contact(request: ASGIRequest):
    if request.method == 'POST':
        try:
            print(request.POST)
            msg = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                          message=request.POST['message'])
            msg.save()

            return render(request, 'contact-us.html', {'msg': 'Message sent successfully!'})
        except Exception as e:
            print(e)
    return render(request, 'contact-us.html')


def books(request: ASGIRequest):
    if request.method == 'POST':
        try:
            PublishBookResponse(
                name=request.POST['full-name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                publish_information=request.POST['information']
            ).save()
            return render(request, 'books.html', {'msg': 'Submitted Successfully'})
        except Exception as e:
            return render(request, 'books.html', {'msg': None})

    return render(request, 'books.html', {'msg': None})
<<<<<<< HEAD
=======


def connect_us(request: ASGIRequest):
    if request.GET['page'] == 'diagnostic':
        if request.method == 'POST':
            diagnostic_listing_enquiry = DiagnosticListingEnquiry(
                name=request.POST['diagnostic-center'],
                contact_person=request.POST['contact-person-name'],
                contact_person_position=request.POST['contact-person-position'],
                contact_person_email=request.POST['contact-person-email'],
                contact_person_phone=request.POST['contact-person-phone'],
                address=request.POST['diagnostics-address'],
            )
            try:
                diagnostic_listing_enquiry.save()
                return render(request, 'connect-diagnostics.html', {'msg': 'Saved Successfully!'})
            except:
                return render(request, 'connect-diagnostics.html', {'msg': 'Something went wrong.'})
        else:
            return render(request, 'connect-diagnostics.html', {})

    elif request.GET['page'] == 'doctor':
        try:
            if request.method == 'POST':
                DoctorListingEnquiry(
                    doctor_name=request.POST['doctor-name'],
                    speciallity=request.POST['speciality'],
                    doctor_email=request.POST['email'],
                    doctor_phone=request.POST['phone'],
                    hospital_name=request.POST['hospital-name'],
                    city=request.POST['city'],
                    hospital_address=request.POST['hospital-address']
                ).save()
                return render(request, 'connect-doctor.html', {'msg': 'Saved Successfully!'})
            else:
                return render(request, 'connect-doctor.html', {})
        except:
            return render(request, 'connect-doctor.html', {'msg': 'Something went wrong'})

    return render(request, '404.html')
>>>>>>> origin/master
