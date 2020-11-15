from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Like(models.Model):
    value = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(1), MinValueValidator(0)]
    )
    user = models.ForeignKey(User, max_length=150, blank=False, null=False, on_delete=models.SET_NULL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
