import uuid
from django.db import models


class CategoryType(models.Model):
    description = models.CharField(max_length=1024)
    form_description = models.CharField(max_length=1024)


class AttributeType(models.Model):
    description = models.CharField(max_length=1024)
    form_description = models.CharField(max_length=1024)
    default_category = models.ForeignKey(CategoryType)
    to_ids = models.BooleanField(default=false)


class AttributeGroup(models.Model):
    description = models.CharField(max_length=1024)
    attributes = models.ManyToManyRel(AttributeType)


# TODO: has many other model dependencies to add first
class Sighting(models.Model):
    pass


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

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    distribution = models.CharField(default=ORGANISATION, choices=DISTRIBUTION_CHOICES, max_length=3)
    creation_date = model.DateTimeField(auto_now_add=true)
    updated_date = model.DateTimeField(auto_now=true)
    attr_type = models.ForeignKey(AttributeType)
    category = models.ForeignKey(CategoryType)
    to_ids = models.BooleanField(default=false)
    deleted = models.BooleanField(default=false)
    comment = models.TextField()
    value = models.TextField()
