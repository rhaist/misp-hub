import uuid
from django.db import models
from django.conf import settings


class Organisation(models.Model):
    # Remote and local org MUST fields
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=False)
    name = models.CharField(max_length=255, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # Optional fields if org is local
    local = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    org_type = models.CharField(max_length=255)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    sector = models.CharField(max_length=255, blank=True)
    contacts = models.TextField(blank=True)
    landingpage = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="org_creator", blank=True)
    nationality = models.CharField(max_length=255, blank=True) # TODO: django-countries ?
    logo = models.ImageField(blank=True)
