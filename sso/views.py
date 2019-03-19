from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializerUtility import MethodSerializerView
from django.contrib.auth.hashers import make_password, check_password
from .customJWT import jwt_payload_handler
from .err import MyErrorException
from rest_framework_jwt.settings import api_settings
from .serializers import (
    RegisterSerializer,
    LoginSerializer
)
from .models import (
    User
)

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

# Create your views here.

class RegisterUserViewset(viewsets.ViewSet, MethodSerializerView):
    """ Registers a User """
    queryset = User.objects.all()
    method_serializer_classes = {
        ('POST'): RegisterSerializer
    }

    def create(self, request, format=None):
        try:
            data = request.data
            f_name = data['f_name']
            l_name = data['l_name']
            email = data['email']
            password = data['password']
            User.objects.create(
                first_name = f_name,
                last_name = l_name,
                email = email,
                password = make_password(password)
            )
        except Exception as Err:
            MyErrorException(Err, "Registering User")
            return Response(status=status.HTTP_400_BAD_REQUEST)  
        return Response(status=status.HTTP_201_CREATED)

class LoginViewset(viewsets.ViewSet, MethodSerializerView):
    """ Login a User """
    queryset = User.objects.all()
    method_serializer_classes = {
        ('POST'): LoginSerializer
    }
    def create(self, request, format=None):
        try:
            data = request.data
            user = User.objects.get(email=data['email'])
            if check_password(data['password'],user.password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as Err:
            MyErrorException(Err, "")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'token':token},status=status.HTTP_200_OK)

class VerifyViewset(viewsets.ViewSet, MethodSerializerView):
    """ Login a User """
    queryset = User.objects.all()
    method_serializer_classes = {
        ('POST')
    }
    def create(self, request, format=None):
        try:
            data = request.data
            payload = jwt_decode_handler(data['token'])
        except Exception as Err:
            MyErrorException(Err, "")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'token': payload},status=status.HTTP_200_OK)