from common.constants import Gender
from common.models import BaseModel
from django.db import models

from .disease_model import Disease


class Patient(BaseModel):
    name = models.CharField(max_length=128, blank=False, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=16, choices=Gender.choices())
    avatar = models.URLField(max_length=128, blank=True, null=True)
    diseases = models.ManyToManyField(Disease, blank=True)

    class Meta:
        db_table = "Patient"
        managed = True
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
