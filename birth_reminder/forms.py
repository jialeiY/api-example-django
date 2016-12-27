from django import forms
from django.forms import ModelForm,Select
from .models import Messages,UserInfo,DoctorMessageMapping
import drchronoAPI
class SettingForm(forms.Form):
    message=forms.CharField()
    send_time=forms.TimeField()
    
class MessageForm(ModelForm):
    
    def __init__(self,*args,**kwargs):
        self.user=kwargs.pop('user')
        super(MessageForm,self).__init__(*args,**kwargs)
        self.fields['message_name'].widget=Select(choices=drchronoAPI.get_user_message_name(self.user))
    
    class Meta:
        model=Messages
        fields=['message_name','message_subject','message_text']
        #widgets={'message_name':Select(choices=drchronoAPI.get_user_message_name(user))}
