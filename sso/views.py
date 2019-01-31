from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializerUtility import MethodSerializerView
from django.contrib.auth.hashers import make_password, check_password
from .err import MyErrorException
from .serializers import (
    RegisterSerializer,
    LoginSerializer
)
from .models import (
    User
)

# Create your views here.

class RegisterUserViewset(viewsets.ViewSet, MethodSerializerView):
    """ Registers a User """
    queryset = User.objects.all()
    method_serializer_classes = {
        ('POST'): RegisterSerializer
    }
    # serializer_class = RegisterSerializer

    def create(self, request, format=None):
        try:
            data = request.data
            f_name = data['f_name']
            l_name = data['l_name']
            email = data['email']
            password = data['password']
            user_creation = User.objects.create(
                first_name = f_name,
                last_name = l_name,
                email = email,
                password = make_password(password)
            )
        except Exception as Err:
            MyErrorException(Err, "Registering User")
            return Response(status=status.HTTP_400_BAD_REQUEST)  
        return Response(status=status.HTTP_201_CREATED)


