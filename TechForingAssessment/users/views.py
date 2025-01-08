from dataclasses import fields

from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView

from users.serializers import TflUserSerializer, TflUserRegisterSerializer


class TflUserRegisterView(CreateAPIView):
    serializer_class = TflUserRegisterSerializer


class TflUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = TflUserSerializer

