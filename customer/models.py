from django.db import models
from owner.models import Mobile

# Create your models here.


class Cart(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    options=(
        ("in_cart","in_cart"),
        ("order_place","order_place"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=40,default="in_cart",choices=options)
    user=models.CharField(max_length=30)

