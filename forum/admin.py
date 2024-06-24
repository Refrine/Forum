from django.contrib import admin

from .models import Forum, Topic, Message

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Message)
