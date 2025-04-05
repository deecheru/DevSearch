from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
import uuid
# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null = True, blank = True)
    email = models.EmailField(max_length=500, null = True, blank = True)
    user_name = models.CharField(max_length=200, null = True, blank = True)
    location = models.CharField(max_length=200, null = True, blank = True)
    bio = models.CharField(max_length=200, null = True, blank = True)
    short_intro = models.TextField(max_length = 2000, null = True, blank=True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = 'profiles.',default = 'profiles/user-default.png')
    social_github = models.CharField(max_length=200, null = True, blank = True)
    social_twitter = models.CharField(max_length=200, null = True, blank = True)
    social_linkedin = models.CharField(max_length=200, null = True, blank = True)
    social_website = models.CharField(max_length=200, null = True, blank = True)
    social_youtube = models.CharField(max_length=200, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)

    def __str__(self):
        return str(self.user_name)

class Skills(models.Model):
    owner = models.ForeignKey(Profiles,on_delete=models.CASCADE, null = True, blank= True)
    name = models.CharField(max_length = 200, null = True, blank = True)
    description = models.TextField(max_length = 2000, null = True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    def __str__(self):
        return str(self.name)

class Message(models.Model):

    sender = models.ForeignKey(Profiles, null = True, on_delete = models.SET_NULL,blank = True)
    recepient = models.ForeignKey(Profiles,on_delete=models.SET_NULL,null = True, blank = True,related_name = "messagesRequests")
    email = models.CharField(max_length = 200, null = True, blank = True)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    body = models.TextField()
    is_read = models.BooleanField(default = False,null = True)
    name = models.CharField(max_length = 200, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']



