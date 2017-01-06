from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MessagesManager(models.Manager):
    def create_message(self,message_name,message_text):
        message=self.create(message_name=message_name,message_text=message_text)
        return message
class Messages(models.Model):
    message_name=models.CharField(max_length=200)
    message_subject=models.CharField(max_length=1000)
    message_text=models.TextField()
    def __str__(self):
        return self.message_name
    objects=MessagesManager()

DEFAULT_MESSAGE_ID=Messages.objects.get(pk=1)

class UserInfoManager(models.Manager):
    def create_user(self,user,doctor_id,send_time='08:00:00',message=DEFAULT_MESSAGE_ID,is_active=True):
        user=self.create(user=user,doctor_id=doctor_id,send_time=send_time,
        message=message,is_active=is_active)
        return user
        
class UserInfo(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    doctor_id=models.IntegerField()
    #username=models.CharField(max_length=200)
    send_time=models.TimeField()
    message=models.ForeignKey(Messages)
    is_active=models.BooleanField()
    def __str__(self):
        return self.user.username
    objects=UserInfoManager()

    """
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    suffix=models.CharField(max_length=200)
    office_phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    job_title=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    """
class DoctorMessageMappingManager(models.Manager):
    def create_mapping(self,user,message):
        mapping=self.create(user=user,message=message)
        return mapping
class DoctorMessageMapping(models.Model):
    user=models.ForeignKey(UserInfo)
    message=models.ForeignKey(Messages)
    
    objects=DoctorMessageMappingManager()
    
    
  
#message=Messages.objects.create_message('default_1','1111111')
#message=Messages.objects.create_message('default_2','222222222222222')
#message=Messages.objects.create_message('default_3','33333333333333')
