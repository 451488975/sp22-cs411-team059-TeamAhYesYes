from django.db import models
from django.urls import reverse
from django.utils import timezone


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    discount = models.FloatField(default=1.0)
    recommender_name = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.username})'

    def get_absolute_url(self):
        return reverse(
            'petshop_customer_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_customer_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_customer_delete_url',
            kwargs={'pk': self.pk}
        )

    class Meta:
        db_table = 'customer'
        ordering = ['first_name', 'last_name', 'username']


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.shop_name}'

    def get_absolute_url(self):
        return reverse(
            'petshop_shop_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_shop_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_shop_delete_url',
            kwargs={'pk': self.pk}
        )

    class Meta:
        db_table = 'shop'
        ordering = ['shop_name']


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, related_name='pets', on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, related_name='pets', on_delete=models.CASCADE, blank=True, default='', null=True
    )
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.age} Days {self.breed} {self.type}'

    def get_absolute_url(self):
        return reverse(
            'petshop_pet_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_pet_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_pet_delete_url',
            kwargs={'pk': self.pk}
        )

    class Meta:
        db_table = 'pet'
        ordering = ['type', 'breed', 'age']


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f'{self.item_name}({self.shop.shop_name})'

    def get_absolute_url(self):
        return reverse(
            'petshop_item_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_item_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_item_delete_url',
            kwargs={'pk': self.pk}
        )

    class Meta:
        db_table = 'item'
        ordering = ['shop__shop_name', 'item_name']


class POrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)
    transaction_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order {self.order_id}'

    def get_absolute_url(self):
        return reverse(
            'petshop_order_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_order_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_order_delete_url',
            kwargs={'pk': self.pk}
        )

    def get_order_total(self):
        contains_list = self.contains.all()
        total_price = 0.0
        for contain in contains_list:
            total_price += contain.item.price * contain.quantity * contain.order.customer.discount
        order = POrder.objects.get(pk=self.pk)
        order.total_price = total_price
        order.save(update_fields=['total_price'])
        return total_price

    class Meta:
        db_table = 'p_order'
        ordering = ['order_id']


class Contains(models.Model):
    contains_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, related_name='contains', on_delete=models.CASCADE)
    order = models.ForeignKey(POrder, related_name='contains', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Contains {self.contains_id}'

    def get_absolute_url(self):
        return reverse(
            'petshop_contains_detail_url',
            kwargs={'pk': self.pk}
        )

    def get_update_url(self):
        return reverse(
            'petshop_contains_update_url',
            kwargs={'pk': self.pk}
        )

    def get_delete_url(self):
        return reverse(
            'petshop_contains_delete_url',
            kwargs={'pk': self.pk}
        )

    class Meta:
        db_table = 'contains'
        ordering = ['contains_id']
