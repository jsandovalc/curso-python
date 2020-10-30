from django.db import models


class BillType(models.IntegerChoices):
    ACUEDUCTO = 1, "Acueducto"
    ALCANTARILLADO = 2, "Alcantarillado"
    ADMINISTRACION = 3, "Administración"
    ENERGIA = 4, "Energía"


class Bill(models.Model):
    nit = models.CharField(max_length=30)

    bill_type = models.IntegerField(choices=BillType.choices, default=BillType.ACUEDUCTO)



class Item(models.Model):
    description = models.CharField(max_length=200)

    quantity = models.IntegerField(default=1)

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
