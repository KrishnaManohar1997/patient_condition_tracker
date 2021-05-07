from patient.services.disease_service import DiseaseService
from django.db.models.query import QuerySet
from patient.models import Patient

class PatientRepository:
    disease_service = DiseaseService()
    
    def get_patients_by_name(self, patient_name:str)->QuerySet[Patient]:
        """Gets all the patients matching the name `patient_name`

        Args:
            patient_name (str): Name of the patients that needs to be retrieved

        Returns:
            QuerySet[Patient]: Queryset of all the patients matching patient_name
        """
        return Patient.objects.filter(name__icontains=patient_name, is_deleted=False)
    
    def get_patients_by_age(self, patient_age:int)->QuerySet[Patient]:
        """Gets all the patients matching the name `patient_age`

        Args:
            patient_age (int): Name of the patients that needs to be retrieved

        Returns:
            QuerySet[Patient]: Queryset of all the patients matching patient_age
        """
        return Patient.objects.filter(age=patient_age, is_deleted=False)
    
    def get_patient_by_id(self,patient_id:str)->Patient:
        """Get a patient instance based on Patient Id

        Args:
            patient_id (str): Id of the patient

        Returns:
            Patient: Instance of the patient
        """
        return Patient.objects.get(id=patient_id)
    
    def assign_disease_to_patient(self, patient_id:str, disease_id:str)->Patient:
        patient = self.get_patient_by_id(patient_id)
        disease =self.disease_service.get_disease_by_id(disease_id)
        patient.dieseases.add(disease)
        patient.save()
        return Patient