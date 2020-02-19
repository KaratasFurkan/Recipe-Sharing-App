from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField(max_length=4000)
    ingredients = models.ManyToManyField("Ingredient")

    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    EASY = "0"
    MEDIUM = "1"
    HARD = "2"
    DIFFICULTY_CHOICES = [
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (HARD, "Hard"),
    ]
    difficulty = models.CharField(
        max_length=1, choices=DIFFICULTY_CHOICES, default=EASY,  # blank=False
    )


class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    recipes = models.ManyToManyField(Recipe)

    # class Meta:
    #     ordering = ['headline']


class Like:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Star:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])