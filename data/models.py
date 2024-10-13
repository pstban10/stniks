from django.db import models
from django.utils import timezone

SEX_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('U', 'UNDEFINED')
]


class Persona(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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


class RmData(models.Model):
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
        return f"los RM's de {self.user.first_name} {self.user.last_name}"
