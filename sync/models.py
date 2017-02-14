import uuid
from django.db import models
from orgs.models import Organisation

class SyncServer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    authkey = models.CharField(max_length=40)
    org_id = models.IntegerField(blank=False)
    push = models.BooleanField(blank=False)
    pull = models.BooleanField(blank=False)
    lastpulledid = models.IntegerField(blank=True)
    lastpushedid = models.IntegerField(blank=True)
    organization = models.ForeignKey(Organisation)
    remote_org_id = models.IntegerField(blank=False)
    self_signed = models.BooleanField(blank=False)
    pull_rules = models.TextField(blank=False)
    push_rules = models.TextField(blank=False)
    cert_file = models.CharField(max_length=255, blank=True)
    client_cert_file = models.CharField(max_length=255, blank=True)
    internal = models.BooleanField(default=0)
