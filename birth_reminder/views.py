# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from social.apps.django_app.default.models import UserSocialAuth
import requests
from django.template import loader
from django.shortcuts import render,render_to_response
from forms import SettingForm,MessageForm
from django.core.urlresolvers import reverse
import drchronoAPI
from .models import Messages
from django.template import RequestContext
def home(request):
    user_info=drchronoAPI.get_user_info(request.user)
    if request.method=='POST':

        message_id=request.POST['id_message_name']
        print message_id
        print Messages.objects.get(pk=message_id)
        message=Messages.objects.get(pk=message_id)

        form=MessageForm(initial={'message_name':message.id},instance=message,user=user_info)
        print {'id_message_subject':message.message_subject,
        'id_message_text':message.message_text}
        return JsonResponse({'id_message_subject':message.message_subject,
        'id_message_text':message.message_text})
        #return render(request,'birth_reminder/home.html',{'form':form})
        #if not form.is_valid():
            #print 'wrong',form
            #form=MessageForm(instance=user_info.message,user=user_info)
        #else:
            #print 'corret',form
    else:   
        form=MessageForm(instance=user_info.message,user=user_info)
    print request
    return render(request,'birth_reminder/home.html',{'form':form})



def patient_list(request):
    column=['last_name','date_of_first_appointment','id',
    'first_name','middle_name','date_of_birth','email',
    'chart_id','gender']
    template=loader.get_template('birth_reminder/patient_list.html')
    user=request.user
    patients=drchronoAPI.get_patient_list(user)
    context={'patients_list':patients,'column':column}
    '''
    response=UserSocialAuth.objects.get(user=user)
    patients_url='https://drchrono.com/api/patients'
    access_token=response.extra_data['access_token']
    headers={'Authorization': 'Bearer {0}'.format(access_token)}
    patients=[]
    while patients_url:
        data=requests.get(patients_url,headers=headers).json()
        patients.extend(data['results'])
        patients_url=data['next']
    context={'patients_list':patients}
    print patients[0]
    '''
    return render(request,'birth_reminder/patient_list.html',context)