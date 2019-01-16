from django.db import models


class DateTimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    class Meta:
        abstract = True

class AbstractStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    cr = models.TimeField(auto_now_add=True)
    mod = models.TimeField(auto_now=True)

    
    class Meta:
        abstract = True