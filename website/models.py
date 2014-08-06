from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Screen(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=255, null=False, blank=True, default='')
    image = models.ImageField(upload_to=getattr(settings, "MEDIA_ROOT"))


class Comment(models.Model):
    screen = models.ForeignKey(Screen)
    created_by_user = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255)


admin.site.register(Screen)
admin.site.register(Comment)

