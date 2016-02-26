"""
Our database is described here
"""

from django.db import models
import datetime
from django.contrib.auth.models import User

"""
begin constants
"""

SEVERITY = (
    (0, 'None'),
    (1, 'Minor'),
    (2, 'Medium'),
    (3, 'Important'),
    (4, 'Critical'),
)

"""
begin tables
"""
class NerdeezModel(models.Model):
    """
    All models will extend this base class
    """

    creation_date = models.DateTimeField(default=datetime.datetime.now())
    modified_data = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(NerdeezModel):
    """
    bugs can have tags
    """

    title = models.CharField(max_length=400)

class Bug(NerdeezModel):
    """
    a bug can be reported by a user and assigned by a user
    """

    user = models.ForeignKey(User, related_name='reported_bugs')
    assigned_user = models.ForeignKey(User, blank=True, null=True, default=None, related_name='assigned_bugs')
    tags = models.ManyToManyField(Tag)
    severity = models.PositiveIntegerField(choices=SEVERITY, default=0)