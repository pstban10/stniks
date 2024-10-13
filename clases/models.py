from django.db import models


class TestClass(models.Model):
    full_name = models.CharField(max_length=150)
    date = models.DateField()
    phone = models.CharField(max_length=20)
    hour = models.TimeField()

    HORARIOS = {
        'lunes': ['8:00', '9:00', '15:00', '18:00', '19:15'],
        'martes': ['18:00', '19:15'],
        'miércoles': ['8:00', '9:00', '15:00', '18:00', '19:15'],
        'jueves': ['18:00', '19:15'],
        'viernes': ['8:00', '9:00', '15:00', '18:00', '19:15'],
        'sábado': ['18:00', '19:15'],
        'domingo': 'not classes buddy'
    }

    def __str__(self):
        return f"{self.full_name} - {self.date}"
