from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import (
    RegisterSerializer,
    LoginSerializer
)
from .models import (
    User
)

# Create your views here.

class RegisterUserViewset(viewsets.ModelViewSet):
    """ Registers a User """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, format=None):
        data = request.data
        f_name = data['f_name']
        l_name = data['l_name']
        email = data['email']
        return Response(status=status.HTTP_200_OK)


