from django.db import models


class Menu(models.Model): 
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=80)
    image = models.ImageField(upload_to='menuimages')
    price = models.DecimalField(max_digits=5, decimal_places=2) 
