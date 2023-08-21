# Generated by Django 4.1 on 2023-08-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('expense_item_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=500)),
                ('item_price', models.FloatField()),
            ],
        ),
    ]
