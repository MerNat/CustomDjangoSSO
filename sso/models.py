from django.db import models
from .core.absmodels import *

class Studio(DateTimeStampedModel,AbstractStampedModel):
    name = models.CharField(max_length=40)