from django.db import models


class Order(models.Model):
    """Model definition for Order."""

    is_delivered = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    details = models.JSONField()
    order_date = models.DateField(auto_now_add=True)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

