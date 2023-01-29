from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MaxValueValidator

from django.db import models
from django.db.models import Model


class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Product(Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    term = models.IntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Payment(Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Delivery(Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name




class Supplier(Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    iban = models.IntegerField()
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    payment_method = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    delivery_method = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Manager(Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)

    def __str__(self):
        return self.first_name


class Supplies(Model):
    create_at = models.DateField(auto_now=True)
    final_price = models.IntegerField()
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class SuppliedProduct(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    supplies = models.ForeignKey('Supplies', on_delete=models.CASCADE)


class Stock(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    expired_at = models.DateField()
    cooker = models.ForeignKey('Cooker', on_delete=models.SET_NULL, null=True)


class CookerRank(Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Cooker(Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)
    rank = models.ForeignKey(CookerRank, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
