# Generated by Django 4.1.5 on 2023-01-29 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_remove_stockhistory_rank_stockhistory_final_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.product'),
        ),
        migrations.AddField(
            model_name='supplierproduct',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.supplier'),
        ),
    ]
