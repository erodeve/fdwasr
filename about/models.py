from django.db import models


class About(models.Model): 
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300) 
    image = models.ImageField(upload_to='aboutimages')

    class Meta:
        verbose_name_plural = 'About content'

    def __str__(self):
        return 'Content for about page (click here to edit)'
