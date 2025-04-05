from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from users.models import Profiles

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(user = user, user_name = user.username,
         email = user.email, name = user.first_name)

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.user_name
        user.email = profile.email
        user.save()

post_save.connect(createProfile, sender = User)
post_delete.connect(deleteUser, sender = Profiles)
post_save.connect(updateUser, sender = Profiles)