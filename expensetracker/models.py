import django.utils.timezone
from django.db import models
from django.utils.timezone import now


# Create your models here.

class ExpenseItem(models.Model):
    expense_item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=500)
    item_price = models.FloatField()
    date = models.DateTimeField(default=django.utils.timezone.now)
