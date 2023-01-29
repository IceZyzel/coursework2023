from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Model


class Measure:
    name = models.CharField(max_length=64)


class Product(Model):
    name = models.CharField(max_length=64)
    term = models.IntegerField()
    measure = models.ForeignKey(Measure)


class Payment(Model):
    name = models.CharField(max_length=64)


class Delivery(Model):
    name = models.CharField(max_length=64)


class Supplier(Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    iban = models.IntegerField()
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    payment_method = models.ForeignKey(Payment, on_delete=models.SET_NULL)
    delivery_method = models.ForeignKey(Delivery, on_delete=models.SET_NULL)


class SupplierProduct(Model):
    product = Product
    supplier = Supplier
    price = models.FloatField()


class Manager(Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)


class SuppliedProduct(Model):
    product = models.ForeignKey(SupplierProduct, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class Supplies(Model):
    create_at = models.DateField(auto_now=True)
    final_price = models.IntegerField()

    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL)


class StockProduct(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    expired_at = models.DateField()


class CookerRank(Model):
    name = models.CharField(max_length=64)


class Cooker(Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)
    rank = models.ForeignKey(CookerRank, on_delete=models.SET_NULL)
