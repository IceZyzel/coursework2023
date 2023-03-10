# Generated by Django 4.0.2 on 2023-01-28 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuppliedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.product')),
                ('supplies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.supplies')),
            ],
        ),
    ]
