from rest_framework import serializers

from sso.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User