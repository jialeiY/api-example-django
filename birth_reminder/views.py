# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from social.apps.django_app.default.models import UserSocialAuth
import requests
from django.template import loader
from django.shortcuts import render,render_to_response
from forms import UserInfoForm
from django.core.urlresolvers import reverse
import drchronoAPI
from .models import Messages
from django.template import RequestContext

def home(request):

    user_info=drchronoAPI.get_user_info(request.user)
    message=user_info.message 
    userForm=UserInfoForm(initial={'msg_subject':message.message_subject,
    'msg_text':message.message_text},instance=user_info)

    return render(request,'birth_reminder/home.html',{'form':userForm})

def update_message(request):
    #print request.POST
    message_id=request.POST['id_message']
    message=Messages.objects.get(pk=message_id)   
    return JsonResponse({'id_message_subject':message.message_subject,
        'id_message_text':message.message_text})
        
def save_message(request):

    user_info=drchronoAPI.get_user_info(request.user)
    form=UserInfoForm(request.POST)

    if form.is_valid():
        if form.cleaned_data['is_active']==True:
            #user_info.message=form.cleaned_data['message']
            user_info.send_time=form.cleaned_data['send_time']
            m=user_info.message
            m.message_subject=form.cleaned_data['msg_subject']
            m.message_text=form.cleaned_data['msg_text']
            m.save()
        user_info.is_active=form.cleaned_data['is_active']
        user_info.save()
    else:
        print 'wrong',form
    return HttpResponseRedirect('/birth_reminder/')    
    
