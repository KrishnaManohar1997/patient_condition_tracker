from patient.serializers import DiseaseSerializer
from rest_framework import viewsets
from patient.models import Disease


class DiseaseViewset(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
