from django.db import models

class HigherConditions(models.Model):
    src_currency = models.CharField(max_length=20)
    condition_price = models.BigIntegerField()
    email = models.EmailField()

class LowerConditions(models.Model):
    src_currency = models.CharField(max_length=20)
    condition_price = models.BigIntegerField()
    email = models.EmailField()
