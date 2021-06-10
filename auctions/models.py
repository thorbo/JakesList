from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchlist = models.ManyToManyField("Listings", blank=True, related_name="watchers")

class Listings(models.Model):
    price = models.FloatField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE, related_name="category_items")
    picture = models.CharField(max_length=512)
    expiration = models.DateTimeField()
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posting")
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winning", blank=True, null=True)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.title} (${self.price})"

class Categories(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

class Bids(models.Model):
     bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
     listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="listing_bids")
     amount = models.FloatField()

class Comments(models.Model):
     comment = models.CharField(max_length=512)
     commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
     listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="listing_comments")

