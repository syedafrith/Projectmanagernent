from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from models.models import TflProjectModel
from users.serializers import TflUserSerializer


class TflProjectSerializer(ModelSerializer):
    owner_details = SerializerMethodField(read_only=True)
    class Meta:
        model = TflProjectModel
        fields = '__all__'

    def get_owner_details(self,obj):
        return TflUserSerializer(User.objects.get(id=obj.owner.id)).data