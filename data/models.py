from django.db import models
from django.utils import timezone


class Persona(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField
    created_on = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rm(models.Model):
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    date_of_medition = models.DateField()
    pull_up = models.IntegerField()
    pull_up_weight = models.IntegerField()
    paralel_dips = models.IntegerField()
    paralel_dips_weight = models.IntegerField()

    def __str__(self):
        return f"los RM's de {self.user.first_name} {self.user.last_name}"
