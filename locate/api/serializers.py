from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,HyperlinkedRelatedField,SerializerMethodField
from locate.models import Zone
from pprint import pprint as pp


class ZoneListSerializer(ModelSerializer):
    class Meta:
        model = Zone
        fields = ("name","position")
        
