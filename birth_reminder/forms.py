from django import forms
from django.forms import ModelForm,Select
from .models import Messages,UserInfo,DoctorMessageMapping
import drchronoAPI

TIME_CHOICES=[]
for h in xrange(24):
    for m in ['00','30']:
        t='{:02d}:{}:00'.format(h,m)
        TIME_CHOICES.append((t,t[:-3]))
   
        
class UserInfoForm(ModelForm):
    msg_subject=forms.CharField(max_length=200)
    msg_text=forms.CharField(max_length=1000,widget=forms.Textarea())
    #def __init__(self,*args,**kwargs):
        #self.user=kwargs.pop('user')
        #super(UserInfoForm,self).__init__(*args,**kwargs)
        #self.fields['message'].choices=drchronoAPI.get_user_message_name(self.user)
    
    class Meta:
        model=UserInfo
        fields=['is_active','send_time']
        widgets={'send_time':forms.Select(choices=TIME_CHOICES)}
        
    def is_valid(self):
        valid=super(UserInfoForm,self).is_valid()
        
        if not valid:
            data=self.cleaned_data
            if data.get('is_active')==False:
                valid=True
        
            
        return valid