from django import forms
from django.forms import ModelForm
from .models import Messages
class SettingForm(forms.Form):
    message=forms.CharField()
    send_time=forms.TimeField()
    
class MessageForm(ModelForm):
    class Meta:
        model=Messages
        fields=['message_name','message_text']