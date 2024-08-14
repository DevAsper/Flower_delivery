# apps/reviews/models.py
from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Product

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review {self.id} by {self.user.username}'
