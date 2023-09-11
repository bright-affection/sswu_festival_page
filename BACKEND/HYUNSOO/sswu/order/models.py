from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='order', null=True)

    def __str__(self):
        return self.name

DATE_CHOICES = [
    ('2023-10-04', '10월 4일'),
    ('2023-10-05', '10월 5일'),
]

TIME_CHOICES = [(f"{i}:00", f"{i}:00") for i in range(11, 20)]

class Reservation(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    user_mail = models.EmailField()
   # goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
   # quantity = models.PositiveIntegerField()
    purchase_date = models.CharField(max_length=10, choices=DATE_CHOICES)
    purchase_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    
class OrderItem(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='item')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.goods.name