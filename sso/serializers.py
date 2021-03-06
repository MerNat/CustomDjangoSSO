from rest_framework import serializers

from sso.models import User

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email','password']