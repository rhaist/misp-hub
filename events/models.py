import uuid
from django.db import models
from django.conf import settings
from events.attribute import Attribute
from orgs.models import Organisation
from sharing_groups.models import SharingGroup


# REF: https://raw.githubusercontent.com/MISP/misp-rfc/master/misp-core-format/raw.md.txt
class Event(models.Model):
    # Some constants to efficiently store choicefields in databases
    INITIAL = 'INI'
    ONGOING = 'ONG'
    COMPLETED = 'COM'

    LOW = 'LOW'
    MEDIUM = 'MED'
    HIGH = 'HIG'

    ANALYSIS_LEVEL_CHOICES = (
        (INITIAL, 'Initial'),
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
    )

    RISK_LEVEL_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    DISTRIBUTION_CHOICES = (
        (0, "Your organisation only"),
        (1, "This community only"),
        (2, "Connected communities"),
        (3, "All communities"),
        (4, "Sharing group"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    published = models.BooleanField(default=False)
    info = models.CharField(blank=False, max_length=256)
    threat_level_id = models.CharField(default=LOW, choices=RISK_LEVEL_CHOICES, max_length=3, blank=True)
    analysis_level = models.CharField(default=INITIAL, choices=ANALYSIS_LEVEL_CHOICES, max_length=3, blank=True)
    # The RFC has 'date' and 'timestamp' we clearify the two here
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # Named 'publish_timestamp' in the RFC but we try to be consistent here
    publish_date = models.DateTimeField(blank=True)
    org_id = models.ForeignKey(Organisation, blank=False)
    orgc_id = models.ForeignKey(Organisation, related_name="owner_org", blank=False)
    distribution = models.IntegerField(default=0, choices=DISTRIBUTION_CHOICES)
    sharing_group_id = models.ForeignKey(SharingGroup, default=0)
    # The original model has 'attribute_count' which we will provide with a
    # model property and reference all included attributes with a relation here.
    attributes = models.ManyToManyField(Attribute)

    @property
    def attribute_count(self):
        return len(self.attributes)


class Sighting(models.Model):
    attribute = models.ForeignKey(Attribute)
    event = models.ForeignKey(Event)
    org = models.ForeignKey(Organisation)
    observation_date = models.DateTimeField(blank=False)


class EventTag(models.Model):
    name = models.CharField(max_length=1024)
    colour = models.CharField(max_length=7) # TODO: django-colorfield?
    exportable = models.BooleanField(default=True)
    hidden = models.BooleanField(default=True)
