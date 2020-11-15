from django.db import models


class Language(models.Model):
    name = models.CharField(null=False, blank=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
