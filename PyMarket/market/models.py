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

    def __str__(self):
        return self.name + " " + str(len(self.items.all()))
