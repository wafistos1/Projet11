from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Categorie(models.Model):
    """
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Class
    """
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    name = models.CharField(_('Nom produit'), max_length=500, unique=True)
    grade = models.CharField(max_length=40)
    images = models.URLField(max_length=500)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    detail_igredient = models.TextField(default='None')
    url = models.URLField(max_length=500, default='None')
    detail_nutrition_url = models.URLField(max_length=500, default='None')
    rate_product = models.IntegerField(max_length=2, choices=RATE_CHOICES, null=True)
    

    def __str__(self):
        return self.name

class Favorite(models.Model):
    """ Class of favorite user
    """

    product_choice = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='PK_product_choice'
        )
    product_favorite = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='PK_product_favorite'
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"produit: {self.product_choice.name} , product_substitute:{self.product_favorite.name}"
