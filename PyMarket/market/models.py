from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    belongs_to = models.ForeignKey("market.items", on_delete=models.CASCADE)
    selling = models.BooleanField(default=False)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.belongs_to.name + " " +  self.owner.username

class items(models.Model):
    name = models.CharField(max_length=500)
    items = models.ManyToManyField("market.item", blank=True)
    image = models.ImageField(upload_to="items-images", blank=True)
    choices = [
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('ultra_rare', 'Ultra rare'),
        ('legendary', 'Legendary'),
    ]
    class rarity_choice(models.TextChoices):
        common = "Common"
        rare = "Rare"
        ultra_rare = "Ultra Rare"
        legendary = "Legendary"
        
    rarity = models.CharField(max_length=100, choices=rarity_choice.choices, default=rarity_choice.common)
    def count_selling(self):
        return len(self.items.all().filter(selling=True))
    def min_price(self):
        if len(self.items.all().filter(selling=True)) > 0:
            return self.items.all().order_by("price")[0].price
        return 0.00
    def __str__(self):
        return self.name + " " + str(len(self.items.all()))
