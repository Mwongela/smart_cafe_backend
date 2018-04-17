from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class FoodCategory(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Food(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)
    calories = models.IntegerField(blank=True, null=True, default=-1)
    price = models.FloatField(blank=False, null=False)
    image = models.ImageField(upload_to='food_imgs', default='static/imgs/default-image-landscape.png')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '{} (KES{})'.format(self.name, self.price)


class MenuCategory(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu(TimeStampedModel):
    date = models.DateField()
    time = models.TimeField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({}, {})'.format(self.category.name, self.date, self.time)


class MenuItem(TimeStampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.food, self.menu)


class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField(blank=False, null=False)

    def __str__(self):
        return '{} - {} - KES{}'.format(self.created, self.user, self.total_amount)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.food, self.order)
