
from social.apps.django_app.default.models import UserSocialAuth
import requests
from .models import UserInfo,DoctorMessageMapping,Messages
from datetime import date,datetime
from string import Template

def get_patient_list(user):
    column=['last_name','first_name','middle_name','date_of_birth','email','gender']
    
    response=UserSocialAuth.objects.get(user=user)
    patients_url='https://drchrono.com/api/patients'
    access_token=response.extra_data['access_token']
    headers={'Authorization': 'Bearer {0}'.format(access_token)}
    patients=[]

    while patients_url:

        data=requests.get(patients_url,headers=headers).json()
        patients_url=data['next']
        print data['results'][0]
        for p in data['results']:            
            new_data={}
            for c in column:
                new_data[c]=p[c]
        
            patients.append(new_data)

    return patients

def get_doctor_info(user,doctor_id):
    response=UserSocialAuth.objects.get(user=user)
    doctors_url='https://drchrono.com/api/doctors'
    access_token=response.extra_data['access_token']
    headers={'Authorization': 'Bearer {0}'.format(access_token)}
    while doctors_url:

        data=requests.get(doctors_url,headers=headers).json()
        doctors_url=data['next']
        for doc in data['results']:
            if doc['id']==doctor_id:
                return doc

    return False
    
DEFAULT_SUBJECT='Happy Birthday to {first_name} from {doctor_first_name} {doctor_last_name}'
DEFAULT_TEXT="""Dear {first_name} {last_name}:
   
Happy birthday to your {age}'s birthday!


{doctor_first_name} {doctor_last_name}
{doctor_office_phone}"""   
    
def get_user_info(user):
    response=UserSocialAuth.objects.get(user=user)    
    access_token=response.extra_data['access_token']
    doctor_id=response.extra_data['doctor']
    try:
        user_info=UserInfo.objects.get(pk=user)
    except UserInfo.DoesNotExist:
        doc_info=get_doctor_info(user,doctor_id)
        subject=combine_doctor_info(doc_info,DEFAULT_SUBJECT)
        text=combine_doctor_info(doc_info,DEFAULT_TEXT)
        m=Messages.objects.create_message(user.username+'_m',subject,text)
        user_info=UserInfo.objects.create_user(user,doctor_id,m)
        set_default_mapping(user_info,m)    
    return user_info
    
def set_default_mapping(user_info,m):
    mapping=DoctorMessageMapping.objects.create_mapping(user_info,m)

class MyTemplate(Template):
    delimiter='{'
    pattern=r'''{(?:
            (?P<escaped>{)|
            (?P<named>[_a-z][_a-z0-9]*)}|
            \b\B(?P<braced>) |
            (?P<invalid>)
    )
    '''   
    
def compare_date(birthd,now=date.today()):
    if not birthd:
        return False
    birthd=datetime.strptime(birthd,'%Y-%m-%d')
    if birthd.month==now.month and birthd.day==now.day:
        return True
    return False

def compute_age(birthd):
    return date.today().year-datetime.strptime(birthd,'%Y-%m-%d').year
    
def combine_text(patient,template):
    patient['age']=compute_age(patient['date_of_birth'])
    template=MyTemplate(template)
    
    return template.safe_substitute(**patient)

def combine_doctor_info(doc_info,template):
    replace={}
    for k,v in doc_info.iteritems():
        replace['doctor_'+k]=v
    template=MyTemplate(template)
    return template.safe_substitute(**replace)
    
def get_user_message(user):
    mapping=DoctorMessageMapping.objects.filter(user=user)
    return mapping
def get_user_message_name(user):
    mapping=get_user_message(user)
    return [(m.message.id,m.message.message_name) for m in mapping]
    
