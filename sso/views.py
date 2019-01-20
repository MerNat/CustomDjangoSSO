from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from .models import *

# Create your views here.

class RegisterUserViewset(viewsets.ModelViewSet):
    """ Registers a User """
    # queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, format=None):
        
        return Response(status=status.HTTP_200_OK)


