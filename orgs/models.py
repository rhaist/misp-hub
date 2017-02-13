import uuid
from django.db import models
from django.conf import settings


class Organisation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    local = models.BooleanField(default=True)
    description = models.CharField(max_length=1024)
    sector = models.CharField(max_length=1024)
    contacts = models.CharField(max_length=1024)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="org_creator")
    nationality = models.CharField(max_length=1024) # TODO: django-countries ?
    logo = models.ImageField()
