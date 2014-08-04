from django.contrib import admin
from django.db import models


class Screen(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=255, null=False, blank=True, default='')
    image = models.ImageField()


class Comment(models.Model):
    screen = models.ForeignKey(Screen)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255)


admin.site.register(Screen)
admin.site.register(Comment)

