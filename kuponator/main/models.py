from django.core.files import images
from django.db import models
from users.models import User

class Kuponi(models.Model):
    title = models.CharField('Магазин', max_length=50)
    description = models.CharField('Описание', max_length=250)
    code = models.CharField('Бонусный код/слово', max_length=250)
    date_exists = models.DateField('До какой даты действует')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Kuponi, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для: {self.user.email} | Продукт {self.products.title}'