from datetime import date

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, default=None)
    birthday = models.DateField(default=date.today())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
