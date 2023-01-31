# Generated by Django 4.1.5 on 2023-01-30 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_supplies_realised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplied_products', to='stock.product'),
        ),
    ]