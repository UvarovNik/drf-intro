from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Sensor
from .serializers import SensorDetailSerializer, SensorSerializer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
