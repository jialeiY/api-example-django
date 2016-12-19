
from social.apps.django_app.default.models import UserSocialAuth
import requests
from .models import UserInfo,DoctorMessageMapping,Messages

def get_patient_list(user):
    
    response=UserSocialAuth.objects.get(user=user)
    patients_url='https://drchrono.com/api/patients'
    access_token=response.extra_data['access_token']
    headers={'Authorization': 'Bearer {0}'.format(access_token)}
    patients=[]

    while patients_url:

        data=requests.get(patients_url,headers=headers).json()           
        patients.extend(data['results'])
        patients_url=data['next']

    return patients

def get_user_info(user):
    response=UserSocialAuth.objects.get(user=user)    
    access_token=response.extra_data['access_token']
    doctor_id=response.extra_data['doctor']
    try:
        user_info=UserInfo.objects.get(pk=doctor_id)
    except UserInfo.DoesNotExist:
        user_info=UserInfo.objects.create_user(doctor_id,user)
        set_default_mapping(user_info)    
    return user_info
    #patients_url='https://drchrono.com/api/doctors'
    #headers={'Authorization': 'Bearer {0}'.format(access_token)}

def set_default_mapping(user_info):
    for id in [1,2,3]:
        mapping=DoctorMessageMapping.objects.create_mapping(user_info,Messages.objects.get(pk=id))
def get_user_message(user):
    mapping=DoctorMessageMapping.objects.filter(user=user)
    return mapping
def get_user_message_name(user):
    mapping=get_user_message(user)
    return [(m.message.id,m.message.message_name) for m in mapping]