from patient.models.patient_model import Patient
from django.db.models.query import QuerySet
from patient.repositories import PatientRepository


class PatientService:
    patient_repo = PatientRepository()
    
    def get_patients_by_name(self, patient_name:str)->QuerySet[Patient]:
        """Gets all the patients matching the name `patient_name`

        Args:
            patient_name (str): Name of the patients that needs to be retrieved

        Returns:
            QuerySet[Patient]: Queryset of all the patients matching patient_name
        """
        return self.patient_repo.get_patients_by_name(patient_name)

    def get_patients_by_age(self, patient_age:int)->QuerySet[Patient]:
        """Gets all the patients matching the name `patient_age`

        Args:
            patient_age (int): Name of the patients that needs to be retrieved

        Returns:
            QuerySet[Patient]: Queryset of all the patients matching patient_age
        """
        return self.patient_repo.get_patients_by_age(patient_age)