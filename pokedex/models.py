from django.db import models
from datetime import date

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(null=False)
    date_of_birth = models.DateField()
    picture = models.ImageField(upload_to="trainer_images", null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
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
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemon_images")

    def __str__(self):
        return self.name
