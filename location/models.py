from cProfile import label
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Loqui(models.Model):
    """Model definition for Loqui."""
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=20)

    class Meta:
        """Meta definition for Loqui."""

        verbose_name = 'Loqui'
        verbose_name_plural = 'Loquis'


class Location(models.Model):
    """Model definition for Location."""

    latitude = models.DecimalField(max_digits=10, decimal_places=6) 
    longitude = models.DecimalField(max_digits=10, decimal_places=6)  
    zoom = models.IntegerField(default=13, validators=[MinValueValidator(0), MaxValueValidator(22)])
    polygon = models.JSONField(
        help_text="""
            To change the delivery area (polygon), change the coordinates inside "coordinates". 
            For example, [lon1, lat1], [lon2, lat2], [lon3, lat3]... [lon1,lat1]
        """
    ) 
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Restaurant location'

    def __str__(self):
        """Unicode representation of Location."""
        return 'Restaurant location/address info (click here to edit)'

