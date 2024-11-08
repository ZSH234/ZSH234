from django.db import models

class Uquvchi(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.IntegerField()
    def __str__(self) -> str:
        return self.ism


