import uuid
from django.db import models
from sharing_groups.models import SharingGroup


class AttributeType(models.Model):
    '''
    An AttributeType consists of a prefix and an optional suffix separated by a
    pipe symbol. For example: domain|ip or filename|sha512
    '''
    description = models.CharField(max_length=1024, blank=True)
    value_prefix = models.TextField(blank=False)
    value_suffix = models.TextField(blank=True)
    to_ids = models.BooleanField(default=False)

    def __str__(self):
        if self.value_suffix.blank:
            return '%s' % (self.value_prefix)
        else:
            return '%s|%s' % (self.value_prefix, self.value_suffix)


class AttributeCategory(models.Model):
    description = models.CharField(max_length=1024)
    attr_types = models.ManyToManyField(AttributeType)


class Attribute(models.Model):
    DISTRIBUTION_CHOICES = (
        (0, 'Your organisation only'),
        (1, 'This community only'),
        (2, 'Connected communities'),
        (3, 'All communities'),
        (4, 'Sharing group'),
        (5, 'Inherit Event'), )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    # Is 'type' in the original model. But this is a keyword in most languages
    # and should not be named this way.
    attr_type = models.ForeignKey(AttributeType, blank=False)
    category = models.ForeignKey(AttributeCategory, blank=False)
    to_ids = models.BooleanField(default=False)
    distribution = models.IntegerField(default=0, choices=DISTRIBUTION_CHOICES)
    # The original model only has 'timestamp' we clearify here
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # Is 'comment' in the original model. But this is a keyword in most sql dialects
    attr_comment = models.TextField(blank=True)
    sharing_group_id = models.ForeignKey(SharingGroup, default=0)
    # 'value1' and 'value2' in the original model
    value_prefix = models.TextField(blank=False)
    value_suffix = models.TextField(blank=False)
    deleted = models.BooleanField(default=False)
