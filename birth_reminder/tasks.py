from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .drchronoAPI import *
from .models import UserInfo
from datetime import date,datetime
from django.core.mail import send_mail



    
@shared_task()
def send_email():
    now=datetime.now()
    print now
    users=UserInfo.objects.filter(is_active=True,send_time='{}:{}'.format(now.hour,now.minute))

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
                email_subject=combine_text(patient,subject)
                email_text=combine_text(patient,text)
                send_mail(email_subject,email_text,doctor.get('email'),
                [email],fail_silently=False)