from django.db import models
from accounts.models import User
from store.models import Product
from django.core.validators import MaxValueValidator
import uuid

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_items')
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return str(self.id)



