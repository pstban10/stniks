from django.db import models

DIAS = [
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miércoles', 'Miercoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
    ('sábado', 'Sabado'),
    ('domingo', 'Domingo')
]
HORARIOS = [
    ('8:00', '8hs'),
    ('9:00', '9hs'),
    ('10:00', '10hs'),
    ('12:00', '12hs'),
    ('14:00', '14hs'),
    ('15:00', '15hs'),
    ('18:00', '18hs'),
    ('19:15', '19hs'),
    ('0', 'what the fak?'),
    ('0', 'not classes buddy'),
    ('0', 'are u sick buddy')
]


class Hours(models.Model):
    weekday = models.CharField(max_length=10, choices=DIAS)
    hour = models.CharField(max_length=5, choices=HORARIOS)

    def __str__(self):
        return f"{self.weekday} - {self.hour}"


class TestClass(models.Model):
    full_name = models.CharField(max_length=150)
    date = models.DateField()
    phone = models.CharField(max_length=20)
    hour = models.ForeignKey(Hours, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.date}"
