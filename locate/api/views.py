from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from locate.api.serializers import ZoneListSerializer

from locate.models import Zone


class ZoneList(ListAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneListSerializer



class ZoneCreate(CreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneListSerializer




