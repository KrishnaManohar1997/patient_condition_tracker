from rest_framework import routers
from .views import PatientViewset,DiseaseViewset

router = routers.DefaultRouter()
router.register(r"patients", PatientViewset)
router.register(r"diseases", DiseaseViewset)
