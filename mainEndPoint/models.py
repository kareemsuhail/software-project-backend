from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core import serializers

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100,unique=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    start_date = models.DateField(default=datetime.datetime.now)
    end_date = models.DateField()
    balance = models.FloatField()
    amount = models.FloatField()

    def as_json(self):

        return serializers.serialize("json", self.get_queryset())
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget,on_delete=models.CASCADE,related_name='budget')
    balance = models.FloatField()
    amount = models.FloatField()
    def __str__(self):
        return self.name
class Expense(models.Model):
    label = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.label + str(self.amount)



