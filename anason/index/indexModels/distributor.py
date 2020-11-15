from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .location import Location


class Distributor(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    country = models.ForeignKey(Location, max_length=150, blank=False, null=False, on_delete=models.SET_NULL)
    city = models.ForeignKey(Location, max_length=150, blank=False, null=False, on_delete=models.SET_NULL)
    postal_code = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(000000)], default=000000)
    address = models.CharField(max_length=150, blank=False, null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
