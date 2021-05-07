from patient.models import Disease

class DiseaseRepository:
    
    def get_disease_by_id(self,disease_id:str)->Disease:
        """Get a Disease instance based on Disease Id

        Args:
            disease_id (str): Id of the Disease

        Returns:
            Disease: Instance of the Disease
        """
        return Disease.objects.get(id=disease_id)
