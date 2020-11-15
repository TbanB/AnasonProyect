from django.urls import path
from .indexViews import anason_index

urlpatterns = [
    path('', anason_index)
]
