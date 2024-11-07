from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

SEX_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('U', 'UNDEFINED')
]


class Persona(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Usuario", on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user.first_name}"


class DateOfMedition(models.Model):
    date_of_medition = models.DateField()

    def __str__(self):
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        dia = self.date_of_medition.day
        mes = meses[self.date_of_medition.month - 1]
        año = self.date_of_medition.year
        return f"{dia:02d} de {mes} del {año}"


class PrData(models.Model):
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    user_weight = models.FloatField(null=True, blank=True)
    date = models.ForeignKey(DateOfMedition, on_delete=models.PROTECT)
    pull_up = models.IntegerField(null=True, blank=True)
    pull_up_weight = models.FloatField(null=True, blank=True)
    paralel_dips = models.IntegerField(null=True, blank=True)
    paralel_dips_weight = models.FloatField(null=True, blank=True)
    skater_squat = models.IntegerField(null=True, blank=True)
    skater_squat_weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"los RM's de {self.user.user.username}"
