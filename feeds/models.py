from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=1024)
    provider = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    rules = models.TextField()
    enabled = models.BooleanField(default=false)
    distribution =
    sharing_group_id =
    tag_id =
