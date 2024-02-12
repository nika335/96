from django.db import models

class Recipe(models.Model):
    name = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
