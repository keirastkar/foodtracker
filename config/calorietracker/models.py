from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Fooditem(models.Model):
    name = models.CharField(max_length=200)
    calorie = models.PositiveIntegerField(default=0)
    carbs = models.FloatField(default=0,null=True,blank=True)
    protein = models.FloatField(default=0,null=True,blank=True)
    fat = models.FloatField(default=0,null=True,blank=True)
    person = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Selectfooditem(models.Model):
    option=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks'),
    )
    name=models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    category=models.CharField(max_length=50,choices=option)
    quantity = models.PositiveIntegerField(default=1)
    person = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.name)


