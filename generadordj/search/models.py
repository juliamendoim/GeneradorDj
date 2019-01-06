from django.db import models
from django_mysql.models import ListCharField

class Lexico(models.Model):
    name = models.CharField(max_length=100)
    lista = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
        default=None
    )
# Create your models here.
