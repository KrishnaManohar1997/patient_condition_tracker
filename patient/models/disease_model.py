from common.models import BaseModel
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from common.constants import DiseaseCategory


class Disease(BaseModel):
    name = models.CharField(max_length=128, blank=False, null=False)
    disease_severity = models.IntegerField(
        validators=[MaxValueValidator(3), MinValueValidator(0)], default=0
    )
    disease_category = models.CharField(
        max_length=32,
        choices=DiseaseCategory.choices(),
        blank=False,
        null=False,
        default=DiseaseCategory.CHRONIC,
    )

    class Meta:
        db_table = "Disease"
        managed = True
        verbose_name = "Disease"
        verbose_name_plural = "Diseases"
