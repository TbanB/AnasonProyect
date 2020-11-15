from django.db import models


class Format(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
