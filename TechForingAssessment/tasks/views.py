from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from models.models import TflTaskModel, TflCommentModel
from tasks.serializers import TflTaskSerializer, TflCommentListSerializer, TflCommentSerializer


# Create your views here.
class TflTaskListView(ListCreateAPIView):
    queryset = TflTaskModel.objects.all()
    serializer_class = TflTaskSerializer

class TflTaskView(RetrieveUpdateDestroyAPIView):
    queryset = TflTaskModel.objects.all()
    serializer_class = TflTaskSerializer

class TflCommentListView(ListCreateAPIView):
    queryset = TflCommentModel.objects.all()
    serializer_class = TflCommentListSerializer

class TflCommentView(RetrieveUpdateDestroyAPIView):
    queryset = TflCommentModel.objects.all()
    serializer_class = TflCommentSerializer