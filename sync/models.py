import uuid
from django.db import models
from orgs.models import Organisation


class SyncServer(models.Model):
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
    publish_without_email = models.BooleanField(default=False)
    unpublish_event = models.BooleanField(default=False)
    pull_rules = models.TextField(blank=False)
    push_rules = models.TextField(blank=False)
    internal = models.BooleanField(default=0)

    # Proxy config
    use_proxy = models.BooleanField(default=False)
    proxy_host = models.CharField(max_length=255, blank=True)
    proxy_port = models.CharField(max_length=255, blank=True)
    proxy_method = models.CharField(max_length=255, blank=True)
    proxy_user = models.CharField(max_length=255, blank=True)
    proxy_pass = models.CharField(max_length=255, blank=True)

    # SSL/TLS config
    cert_file = models.CharField(max_length=255, blank=True)
    ssl_cafile = models.CharField(max_length=255, blank=True)
    client_cert_file = models.CharField(max_length=255, blank=True)
    ssl_local_cert = models.CharField(max_length=255, blank=True)
    self_signed = models.BooleanField(blank=False)
