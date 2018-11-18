from django.db import models
from order.models import Order
from user.models import Stuff


class Review(models.Model):
    STARS_CHOCIES = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Sarts'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STARS_CHOCIES, default=0)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.order.customer}-{self.stuff.position}-{self.stars}'
