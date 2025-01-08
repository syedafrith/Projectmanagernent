from rest_framework.serializers import ModelSerializer

from models.models import TflTaskModel, TflCommentModel


class TflTaskListSerializer(ModelSerializer):
    class Meta:
        model = TflTaskModel
        fields = '__all__'

class TflTaskSerializer(ModelSerializer):
    class Meta:
        model = TflTaskModel
        fields = '__all__'

class TflCommentListSerializer(ModelSerializer):
    class Meta:
        model = TflCommentModel
        fields = '__all__'

class TflCommentSerializer(ModelSerializer):
    class Meta:
        model = TflCommentModel
        fields = '__all__'