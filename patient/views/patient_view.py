from patient.serializers.patient_serializer import PatientDiseaseSerializer
from rest_framework import viewsets
from patient.models import Patient


class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDiseaseSerializer
