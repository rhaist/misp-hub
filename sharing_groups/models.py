from django.db import models


class SharingGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    description = models.TextField()
    creation_date = model.DateTimeField(auto_now_add=true)
    updated_date = model.DateTimeField(auto_now=true)
    active = models.BooleanField(default=false)
