import uuid
from django.db import models
from django.conf import settings
from events.attribute import Attribute


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

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    misp_version = models.CharField(default=settings.MISP_VERSION, max_length=8)
    published = models.BooleanField(default=false)
    creation_date = model.DateTimeField(auto_now_add=true)
    updated_date = model.DateTimeField(auto_now=true)
    publish_date = model.DateTimeField()
    info = models.CharField(max_length=1024)
    analysis_level = models.CharField(default=INITIAL, choices=ANALYSIS_LEVEL_CHOICES, max_length=3)
    threat_level_id = models.CharField(default=LOW, choices=RISK_LEVEL_CHOICES, max_length=3)
    distribution = models.CharField(default=ORGANISATION, choices=DISTRIBUTION_CHOICES, max_length=3)
    proposal_email_lock = models.BooleanField(default=false)
    locked = models.BooleanField(default=false)
    org_id = models.ForeignKey()
    org_owner_id = models.ForeignKey()
    sharing_group_id = models.ForeignKey()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    attributes = models.ManyToManyRel(Attribute)
    tags = models.ManyToManyRel(EventTag)
