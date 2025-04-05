from django.contrib import admin

from .models import Profiles, Skills, Message

# Register your models here.

admin.site.register(Profiles)
admin.site.register(Skills)
admin.site.register(Message)
