from django.db import models
from .core.absmodels import *

# Create your models here.

class Studio(DateTimeStampedModel,AbstractStampedModel):
    name = models.CharField(max_length=40)