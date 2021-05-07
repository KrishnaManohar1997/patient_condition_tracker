from patient.repositories import DiseaseRepository
from patient.models import Disease


class DiseaseService:
    disease_repo = DiseaseRepository()
    
    def get_disease_by_id(self,disease_id:str)->Disease:
        """Get a Disease instance based on Disease Id

        Args:
            disease_id (str): Id of the Disease

        Returns:
            Disease: Instance of the Disease
        """
        return self.disease_repo.get_disease_by_id(id=disease_id)
