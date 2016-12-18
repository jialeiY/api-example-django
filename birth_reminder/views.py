# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from social.apps.django_app.default.models import UserSocialAuth
import requests
from django.template import loader
from django.shortcuts import render
from forms import SettingForm,MessageForm
from django.core.urlresolvers import reverse
def home(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            print 'correct',form['message']
            return HttpResponseRedirect(reverse('birth_reminder:home'))
        else:
            print 'wrong',form
            return HttpResponseRedirect(reverse('birth_reminder:home'))
    else:
        form=MessageForm()
    return render(request,'birth_reminder/home.html',{'form':form})


def patient_list(request):
    colume=['last_name','date_of_first_appointment','updated_at','id',
    'first_name','middle_name','date_of_birth','email','date_of_last_appointment',
    'chart_id','gender',]
    template=loader.get_template('birth_reminder/patient_list.html')
    user=request.user
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
    return render(request,'birth_reminder/patient_list.html',context)