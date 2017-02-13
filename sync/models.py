import uuid
from django.db import models
from orgs.models import Organisation

class Servers(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    authkey = models.CharField(max_length=40)
    org_id = models.IntegerField(null=False)
    push = models.BooleanField()
    pull = models.BooleanField()
    lastpulledid = models.IntegerField(null=False)
    lastpushedid = models.IntegerField(null=False)
    organization = models.ForeignKey(to=Organisation)
    remote_org_id = models.IntegerField(null=False)
    self_signed = models.BooleanField()
    pull_rules = models.TextField()
    push_rules = models.TextField()
    cert_file = models.CharField(max_length=1024)
    client_cert_file = models.CharField(max_length=1024)
    internal = models.BooleanField(default=True)
