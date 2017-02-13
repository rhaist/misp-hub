from django.db import models
from django.conf import settings


class Organisation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    creation_date = model.DateTimeField(auto_now_add=true)
    updated_date = model.DateTimeField(auto_now=true)
    members = models.ManyToManyRel(settings.AUTH_USER_MODEL)
    local = models.BooleanField(default=true)
    description = models.CharField(max_length=1024)
    sector = models.CharField(max_length=1024)
    contacts = models.CharField(max_length=1024)
    created_by = models.ManyToManyRel(settings.AUTH_USER_MODEL)
    nationality = models.CharField(max_length=1024) # TODO: django-countries ?
    logo = models.ImageField()
