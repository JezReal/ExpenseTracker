from django.db import models


# Create your models here.

class ExpenseItem(models.Model):
    expense_item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=500)
    item_price = models.FloatField()
