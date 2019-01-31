from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
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

class RegisterUserViewset(viewsets.ModelViewSet):
    """ Registers a User """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, format=None):
        try:
            serializer = RegisterSerializer(request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            data = request.data
            f_name = data['f_name']
            l_name = data['l_name']
            email = data['email']
            password = data['password']
            user_creation = User.objects.create(
                f_name = f_name,
                l_name = l_name,
                email = email,
                password = make_password(password)
            )
        except Exception as Err:
            MyErrorException(Err, "Registering User")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = RegisterSerializer(user_creation)    
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


