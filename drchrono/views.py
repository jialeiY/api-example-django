# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from social.apps.django_app.default.models import UserSocialAuth
import requests
from django.template import loader
from django.shortcuts import render

def welcome(request):
    template=loader.get_template('drchrono/welcome.html')
    user=request.user
    response=UserSocialAuth.objects.get(user=user)
    patients_url='https://drchrono.com/api/patients'
    access_token=response.extra_data['access_token']
    headers={'Authorization': 'Bearer {0}'.format(access_token)}
    patients=[]
    while patients_url:
        data=requests.get(patients_url,headers=headers).json()
        print data['results']
        patients.extend(data['results'])
        patients_url=data['next']
    context={'patients_list':patients}
    return render(request,'drchrono/welcome.html',context)