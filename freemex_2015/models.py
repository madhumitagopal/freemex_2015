from django.db import models
from django.db.models import Q

# Create your models here.
class freemexUser(models.Model):
	username=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	phonenumber=models.CharField(max_length=20)
	cumulative_asset=models.IntegerField()
	initial_amount=models.IntegerField(default=100000)
	profit=models.IntegerField(default=0)
def __str__(self):
    return self

class allStocks(models.Model):
	name=models.CharField(max_length=100)
	code=models.CharField(max_length=100)
	price=models.IntegerField()
def __str__(self):
    return self
class assets(models.Model):
	user_id=models.ForeignKey(freemexUser)
	stock_id=models.ForeignKey(allStocks)
	quantity=models.IntegerField(default=0)
def __str__(self):
    return self