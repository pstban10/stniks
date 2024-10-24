from django.db import models

WOD_TYPE_CHOICES = [
    ('Pull Horizontal', 'Pull Horizontal'),
    ('Pull Vertical', 'Pull Vertical'),
    ('Push Básico', 'Push Básico'),
    ('Legs Posterior', 'Legs Posterior'),
    ('Legs anterior', 'Legs anterior'),
    ('Abdominales', 'Abdominales'),
    ('Plancha', 'Plancha'),
    ('FrontLever', 'FrontLever'),
    ('Resistencia', 'Resistencia'),
    ('Movilidad', 'Movilidad')
]
DIFFICULTYES = [
    ('1', 'Super Principiante'),
    ('2', 'Principiante'),
    ('3', 'Basico'),
    ('4', 'Duro'),
    ('5', 'Posible'),
    ('6', 'Dificil'),
    ('7', 'Muy dificil'),
    ('8', 'Profesional'),
    ('9', 'Elite'),
    ('10', 'Imposible')
]


class Ejercicio(models.Model):
    name = models.CharField(max_length=200)
    wod_type = models.CharField(max_length=25, choices=WOD_TYPE_CHOICES)
    difficult = models.CharField(max_length=25, choices=DIFFICULTYES)

    def __str__(self):
        return f"{self.name}"
