from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rate(models.Model):
    name = models.CharField(max_length=155, blank=False, null=False)
    value = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
