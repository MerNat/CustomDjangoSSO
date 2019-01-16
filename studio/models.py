from django.db import models
from core.abs-models import *

# Create your models here.

class Studio(TimeStampedModels):
    name = models.CharField(max_length=40)