import uuid
from django.db import models
from django.conf import settings
from events.attribute import Attribute
from orgs.models import Organisation
from sharing_groups.models import SharingGroup


class EventTag(models.Model):
    name = models.CharField(max_length=1024)
    colour = models.CharField(max_length=7) # TODO: django-colorfield?
    exportable = models.BooleanField(default=True)
    hidden = models.BooleanField(default=True)


class Event(models.Model):
    # Some constants to efficiently store choicefields in databases
    INITIAL = 'INI'
    ONGOING = 'ONG'
    COMPLETED = 'COM'

    LOW = 'LOW'
    MEDIUM = 'MED'
    HIGH = 'HIG'

    ORGANISATION = 'ORG'
    COMMUNITY = 'COM'
    CONNECTED_COMMUNITIES = 'CON'
    ALL_COMMUNITIES = 'ACO'
    SHARING_GROUP = 'SHG'

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
        (ORGANISATION, "Your organisation only"),
        (COMMUNITY, "This community only"),
        (CONNECTED_COMMUNITIES, "Connected communities"),
        (ALL_COMMUNITIES, "All communities"),
        (SHARING_GROUP, "Sharing group"),
    )

    # We also add the current MISP feature version to the db
    misp_version = models.CharField(default=settings.MISP_VERSION, max_length=8)
    # Original model fields mostly like the MYSQL.sql file in the original MISP distribution
    org_id = models.ForeignKey(Organisation)
    # The original model has 'date' and 'timestamp' we clearify the two here
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    info = models.TextField(blank=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    published = models.BooleanField(default=False)
    analysis_level = models.CharField(default=INITIAL, choices=ANALYSIS_LEVEL_CHOICES, max_length=3)
    org_owner_id = models.ForeignKey(Organisation, related_name="owner_organisation")
    distribution = models.CharField(default=ORGANISATION, choices=DISTRIBUTION_CHOICES, max_length=3)
    sharing_group_id = models.ForeignKey(SharingGroup)
    proposal_email_lock = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    threat_level_id = models.CharField(default=LOW, choices=RISK_LEVEL_CHOICES, max_length=3)
    # Named 'publish_timestamp' in the original model but we try to be consistent here
    publish_date = models.DateTimeField(blank=True)
    # The original model has 'attribute_count' which we will provide with a
    # model function and reference all included Attributes with a FK here.
    attributes = models.ManyToManyField(Attribute)


class Sighting(models.Model):
    attribute = models.ForeignKey(Attribute)
    event = models.ForeignKey(Event)
    org = models.ForeignKey(Organisation)
    observation_date = models.DateTimeField(blank=False)
