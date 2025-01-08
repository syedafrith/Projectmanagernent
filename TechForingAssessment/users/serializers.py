from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class TflUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password","date_joined")

class TflUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","date_joined")