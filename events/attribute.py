import uuid
from django.db import models
from sharing_groups.models import SharingGroup

class CategoryType(models.Model):
    description = models.CharField(max_length=1024)
    form_description = models.CharField(max_length=1024)


class AttributeType(models.Model):
    description = models.CharField(max_length=1024)
    form_description = models.CharField(max_length=1024)
    default_category = models.ForeignKey(CategoryType)
    to_ids = models.BooleanField(default=False)


class AttributeGroup(models.Model):
    description = models.CharField(max_length=1024)
    attributes = models.ManyToManyField(AttributeType)


class Attribute(models.Model):
    ORGANISATION = 'ORG'
    COMMUNITY = 'COM'
    CONNECTED_COMMUNITIES = 'CON'
    ALL_COMMUNITIES = 'ACO'
    SHARING_GROUP = 'SHG'

    DISTRIBUTION_CHOICES = (
        (ORGANISATION, "Your organisation only"),
        (COMMUNITY, "This community only"),
        (CONNECTED_COMMUNITIES, "Connected communities"),
        (ALL_COMMUNITIES, "All communities"),
        (SHARING_GROUP, "Sharing group"),
    )

    category = models.ForeignKey(CategoryType, blank=False)
    # Is 'type' in the original model. But this is a keyword in most languages
    # and should not be named this way.
    attr_type = models.ForeignKey(AttributeType, blank=False)
    value1 = models.TextField(blank=False)
    value2 = models.TextField(blank=False)
    to_ids = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    # The original model only has 'timestamp' we clearify here
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    distribution = models.CharField(default=ORGANISATION, choices=DISTRIBUTION_CHOICES, max_length=3)
    sharing_group_id = models.ForeignKey(SharingGroup)
    # Is 'comment' in the original model. But this is a keyword in most sql dialects
    attr_comment = models.TextField()
    deleted = models.BooleanField(default=False)
