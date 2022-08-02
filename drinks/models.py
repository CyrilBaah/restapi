from select import select
from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name