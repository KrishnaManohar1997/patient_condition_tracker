import uuid

from django.db import models



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
