from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .drchronoAPI import get_patient_list,get_doctor_info
from .models import UserInfo
from datetime import date,datetime
from django.core.mail import send_mail

def compare_date(birthd,now=date.today()):
    if not birthd:
        return False
    birthd=datetime.strptime(birthd,'%Y-%m-%d')
    if birthd.month==now.month and birthd.day==now.day:
        return True
    return False

def compute_age(birthd):
    return date.today().year-datetime.strptime(birthd,'%Y-%m-%d').year
    
def combine_text(template,patient,doctor):
    replace_string=patient.copy()
    for k,v in doctor.iteritems():
        replace_string['doctor_'+k]=v
    replace_string['age']=compute_age(patient['date_of_birth'])
    #print replace_string
    return template.format(**replace_string)

    
@shared_task
def send_email():
    print 'send email'
    users=UserInfo.objects.filter(is_active=True)
    print 'users',users
    for user in users:
        patient_list=get_patient_list(user.user)
        message=user.message
        subject=message.message_subject
        text=message.message_text
        doctor=get_doctor_info(user.user,user.doctor_id)
        for patient in patient_list:
            if compare_date(patient['date_of_birth']):
                #print patient
                email=patient['email']
                email_subject=combine_text(subject,patient,doctor)
                email_text=combine_text(text,patient,doctor)
                send_mail(email_subject,email_text,doctor.get('email'),
                [email],fail_silently=False)