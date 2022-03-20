from django.db import models


class Homecontent(models.Model):
    """Model definition for Homecontent."""

    welcomeline = models.CharField(max_length=70)
    menuline = models.CharField(max_length=200)
    titleslideone = models.CharField(max_length=40)
    descriptionslideone = models.TextField(max_length=200)
    imageslideone = models.ImageField(upload_to='homeimages')
    titleslidetwo = models.CharField(max_length=40)
    descriptionslidetwo = models.TextField(max_length=200)
    imageslidetwo = models.ImageField(upload_to='homeimages')
    facebooklink = models.URLField(max_length=200)
    youtubelink = models.URLField(max_length=200)
    instagramlink = models.URLField(max_length=200)


    class Meta:
        """Meta definition for Homecontent."""
        verbose_name = 'Homecontent'
        verbose_name_plural = 'Home content'

    def __str__(self):
        """Unicode representation of Homecontent."""
        return 'Home content (click here to edit)'


class Mapboxtoken(models.Model):
    """Model definition for Mapboxtoken."""

    token = models.CharField(max_length=500)

    class Meta:
        """Meta definition for Mapboxtoken."""

        verbose_name = 'Mapboxtoken'
        verbose_name_plural = 'Mapbox token'

    def __str__(self):
        """Unicode representation of Mapboxtoken."""
        return "Mapbox token (click here to edit)"
