from rest_framework import serializers
from patient.models import Patient
from .disease_serializer import DiseaseSerializer


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "age", "gender", "avatar"]


class PatientDiseaseSerializer(PatientSerializer):
    diseases = DiseaseSerializer(many=True)

    class Meta:
        model = Patient
        fields = ["id", "name", "age", "gender", "avatar", "diseases"]
