from django import forms
from django.forms import ModelForm,Select
from .models import Messages,UserInfo,DoctorMessageMapping
import drchronoAPI
    
class MessageForm(ModelForm):
    
    def __init__(self,*args,**kwargs):
        self.user=kwargs.pop('user')
        super(MessageForm,self).__init__(*args,**kwargs)
        self.fields['message_name'].widget=Select(choices=drchronoAPI.get_user_message_name(self.user))
    
    class Meta:
        model=Messages
        fields=['message_name','message_subject','message_text']
class UserInfoForm(ModelForm):
    msg_subject=forms.CharField(max_length=200)
    msg_text=forms.CharField(max_length=1000,widget=forms.Textarea)
    def __init__(self,*args,**kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['message'].choices=drchronoAPI.get_user_message_name(kwargs['instance'])
    
    class Meta:
        model=UserInfo
        fields=['is_active','send_time','message']

