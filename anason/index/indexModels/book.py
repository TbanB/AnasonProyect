import uuid
from datetime import date

from django.db import models

from .language import Language
from .distributor import Distributor
from .rate import Rate
from .category import Category
from .format import Format
from .author import Author

from .like import Like


class Book(models.Model):
    ref = models.CharField(max_length=36, blank=False, null=False, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Distributor, blank=False, on_delete=models.SET_NULL)
    release_date = models.DateField(blank=False, null=False, editable=True,
                                    default=date.today())
    rate = models.ForeignKey(Rate, blank=False, on_delete=models.SET_NULL)
    like = models.ForeignKey(Like, blank=False, on_delete=models.SET_NULL)
    url_image = models.CharField(blank=False, null=False)
    format = models.ForeignKey(Format, blank=False, on_delete=models.SET_NULL)
    isbn = models.CharField(blank=False, null=False)
    pages = models.IntegerField(blank=False, null=False)
    language = models.ForeignKey(Language, blank=False, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank=False, on_delete=models.SET_NULL)
    price = models.FloatField(blank=False, null=False, default=0.0)
    stock = models.IntegerField(blank=False, null=False, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
