from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255, null=True, blank = True)
    shipping_city = models.CharField(max_length=255)
    shipping_region = models.CharField(max_length=255, null=True, blank = True)
    shipping_cap = models.CharField(max_length=255, null=True, blank = True)
    shipping_country = models.CharField(max_length=255)

    #Per non far in modo tale che Shipping Address venga messo al plurale (per comodità)
    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
    
    #Creazione Profilo Personale Utente (DEFAULT) per quando si è appena REGISTRATO
    def create_shipping(sender, instance, created, **kwargs):
        if created:
            user_shipping = ShippingAddress(user=instance)
            user_shipping.save()

    #Automatizzazione del processo
    post_save.connect(create_shipping, sender=User)
    
#Creazione Modello degli ordini
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True) 
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    shipping_address1 = models.TextField(max_length=15000)
    amount_paid = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'

#Creazione Modello degli oggetti degli ordini
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True) 

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.IntegerField(default=1)

    def __str__(self):
        return f'Order Item - {str(self.id)}'