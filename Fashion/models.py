from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):

    desc= models.TextField()
    img= models.ImageField(upload_to='pictures')
    price= models.IntegerField()
    offer = models.IntegerField()
    category = models.IntegerField(default=0)
    status = models .BooleanField (default= False)

    def __str__(self):
        return self.desc

class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    index = models.ForeignKey(Item,on_delete=models.CASCADE)
    address = models.TextField()
    locality = models.CharField(max_length=50)
    pincode = models.IntegerField()
    mob_no = models.BigIntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    qty = models.IntegerField()


    def __str__(self):
        return self.index
