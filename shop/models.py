from django.db import models


class Seller(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    
    def __str__(self):
        return self.name
    
class Lot(models.Model):
    COLOR_CHOICES = [
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('Y', 'Yellow'),
    ('W', 'White'),
]
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    flower_name = models.CharField(verbose_name='Название цветка', max_length=100)
    color = models.CharField(choices=COLOR_CHOICES, max_length=1)
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    is_publish = models.BooleanField(verbose_name='Опубликовать')
    
    def __str__(self):
        return f'{self.flower_name}: {self.quantity}шт. {self.seller}, Цена:{self.price}'
    
class Feedback(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    
class Deal(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    lot = models.ForeignKey(Lot, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Статус сделки', null=True, blank=True)
    
    def get_sum_deal(self):
        return self.lot.price * self.quantity

    def __str__(self):
        return f'Продавец: {self.seller}, Покупатель: {self.customer}, купил {self.lot.flower_name} {self.quantity}шт.'
    
class Status(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
