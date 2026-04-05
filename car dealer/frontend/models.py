from django.db import models
from django.contrib.auth.models import User

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    sentiment = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.dealer.name}"