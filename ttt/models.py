
from django.db import models

class MachinePath(models.Model):
    id = models.CharField(primary_key=True, max_length=30)

class MachineChoice(models.Model):
    option = models.CharField(max_length=2)
    value = models.FloatField()
    path = models.ForeignKey(MachinePath, on_delete= models.CASCADE)
