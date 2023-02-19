from django.db import models
from datetime import *
from django.contrib.auth.models import User

# Create your models here.

class NewContent(models.Model):
    product = models.CharField("Продукт", max_length=50)
    price = models.FloatField("Цена")
    autor = models.CharField("Продавец", max_length=50)
    description = models.TextField("Описание")
    count_viwes = models.IntegerField(default=0)
    date_of_publication = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "NewContent"
        verbose_name_plural = "NewContent"


class Payment(models.Model):
    card = models.IntegerField("Номер карты")
    cvv_kod = models.IntegerField("3 цифры")
    date_of_kart = models.IntegerField("дата действия")
    owner = models.CharField("Владелец", max_length=50)

    def __str__(self):
        return self.card

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payment"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Basket(models.Model):
    username = models.CharField('user', max_length=50)
    product = models.CharField('product', max_length=50)
    id_product = models.IntegerField('id')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "basket"
        verbose_name_plural = "basket"


class ProductView(models.Model):
    product = models.OneToOneField(NewContent, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)