from django.db import models


class LocationLevel(models.IntegerChoices):
    country = 0
    region = 1
    province = 2
    city = 3


class Location(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    level = models.CharField(choices=LocationLevel, blank=False, null=False, default=LocationLevel.country)
    parent = models.ForeignKey('self', blank=False, null=False, default=None, on_delete=models.SET_NULL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.level != LocationLevel.country and self.level <= self.parent.level:
            raise ValueError
