# Generated by Django 4.0.2 on 2023-01-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_supplierproduct_remove_suppliedproduct_supplies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockhistory',
            name='rank',
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='final_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='initial_amount',
            field=models.IntegerField(default=1),
        ),
    ]
