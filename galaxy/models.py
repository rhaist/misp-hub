from django.db import models

class Galaxy(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    galaxy_type =
    description = models.TextField()
    version = models.CharField(max_length=1024)
