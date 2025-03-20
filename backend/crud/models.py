from django.db import models # type: ignore

class Customer(models.Model):
    idCliente = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_customer"