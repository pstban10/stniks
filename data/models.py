from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

SEX_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('U', 'UNDEFINED')
]


class Persona(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Usuario(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Usuario",
        on_delete=models.CASCADE)
    name = models.ForeignKey(Persona, on_delete=models.CASCADE)
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

    # formula de Brzycki: 1RM = Peso / (1.0278 - (0.0278 x Repeticiones))
    def maxRepParalelDips(self):
        if isinstance(self.paralel_dips, (int, float)) and isinstance(self.paralel_dips_weight, (int, float)):
            dips_max = int(int(self.paralel_dips_weight) /
                           (1.0278 - (0.0278 * int(self.paralel_dips))))
            return dips_max
        return 0

    def maxRepPullUp(self):
        if isinstance(self.pull_up, (int, float)) and isinstance(self.pull_up_weight, (int, float)):
            pull_max = int(int(self.pull_up_weight) /
                           (1.0278-(0.0278 * int(self.pull_up))))
            return pull_max
        return 0

    def __str__(self):
        return f"Numeros de {self.user.name}"


class Records(models.Model):
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    records = models.ForeignKey(PrData, on_delete=models.CASCADE)

    def __str__(self):
        return f"los Pr's de {self.user.name}"
