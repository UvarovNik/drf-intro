from django.urls import path

from .views import SensorDetailView, SensorListView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/<pk>/', SensorDetailView.as_view(), name='sensor-detail'),
]
