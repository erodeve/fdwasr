from django.db import models


class Contactcontent(models.Model):
    """Model definition for Contactcontent."""

    title = models.CharField(max_length=30)
    content = models.TextField(max_length=200)

    class Meta:
        """Meta definition for Contactcontent."""

        verbose_name_plural = 'Contact content'

    def __str__(self):
        """Unicode representation of Contactcontent."""
        return 'Content for contact page (click here to edit)'



class Message(models.Model): 
    phone =models.PositiveBigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)
    sent_on = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    

