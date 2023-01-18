from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _

class Room(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, default='Description')
    created_date = models.DateField(_("Date"), default=datetime.date.today)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
