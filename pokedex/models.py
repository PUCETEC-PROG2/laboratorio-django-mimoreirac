from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('G', 'Grass'),
        ('W', 'Water'),
        ('F', 'Fire'),
        ('E', 'Electric'),
        ('R', 'Rock'),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(default=1)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"