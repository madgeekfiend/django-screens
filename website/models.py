from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class ProductTeam(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Screen(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=255, null=False, blank=True, default='')
    image = models.ImageField()
    team = models.ForeignKey(ProductTeam)


class Comment(models.Model):
    screen = models.ForeignKey(Screen)
    created_by_user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255)


admin.site.register(Screen)
admin.site.register(Comment)
admin.site.register(ProductTeam)
