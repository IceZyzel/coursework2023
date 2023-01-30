from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Model


class Measure(Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(Model):
    name = models.CharField(max_length=64)
    term = models.IntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.name


class SupplierProduct(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.product.name}"


class Manager(Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class SuppliedProduct(Model):
    product = models.ForeignKey(SupplierProduct, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class Supplies(Model):
    create_at = models.DateField(auto_now=True)
    final_price = models.IntegerField()

    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StockProduct(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    expired_at = models.DateField()

    def __str__(self):
        return self.name


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

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class StockHistory(models.Model):
    stock = models.ForeignKey(StockProduct, on_delete=models.CASCADE)
    amount = models.IntegerField()
    initial_amount = models.IntegerField(default=1)
    final_amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock.name