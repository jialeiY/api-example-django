from django.db import models

# Create your models here.
class MessagesManager(models.Manager):
    def create_message(self,message_name,message_text):
        message=self.create(message_name=message_name,message_text=message_text)
        return message
class Messages(models.Model):
    message_name=models.CharField(max_length=200)
    message_text=models.TextField()
    def __str__(self):
        return self.message_name
    objects=MessagesManager()

class UserInfo(models.Model):
    doctor_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=200)
    send_time=models.TimeField()
    message_id=models.ForeignKey(Messages)
    def __str__(self):
        return self.username
    """
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    suffix=models.CharField(max_length=200)
    office_phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    job_title=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    """

    
    
    
    
message=Messages.objects.create_message('default_1','1111111')
message=Messages.objects.create_message('default_2','222222222222222')
message=Messages.objects.create_message('default_3','33333333333333')