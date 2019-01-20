from django.db import models
from .core.absmodels import *

class User(DateTimeStampedModel):
    USER_TYPE = (
        ('ADM', 'Administrator'),
        ('MEM', 'Member')
    )
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=40,null=False)
    last_name = models.CharField(max_length=40,null=False)
    user_typ = models.CharField(max_length=3,default='MEM')
    email = models.EmailField(unique=True, max_length=100, null=False)
    password = models.CharField(max_length=200, null=False)