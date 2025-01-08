from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from models.models import TflProjectModel
from projects.serializers import TflProjectSerializer


# Create your views here.

class TflProjectListView(ListCreateAPIView):
    queryset = TflProjectModel.objects.all()
    serializer_class = TflProjectSerializer

class TflProjectView(RetrieveUpdateDestroyAPIView):
    queryset = TflProjectModel.objects.all()
    serializer_class = TflProjectSerializer
