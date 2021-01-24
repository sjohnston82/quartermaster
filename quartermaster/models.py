from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse


from autoslug import AutoSlugField
from django.utils.formats import get_format




class Grocerylist(models.Model):
    item_name = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed_boolean = models.BooleanField(default=False)
    

    def __str__(self):
        return self.item_name



class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quartermaster:mypantry')

class AmountType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quartermaster:mypantry')



class PantryItem(models.Model):
    item_name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    getting_low = models.BooleanField(default=False)
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='item_name', unique=True, editable=False)
    
    quantity = models.PositiveIntegerField(null=False, default=0)
    category = models.CharField(max_length=222)
    to_grocery = models.BooleanField(default=False)
    amount_type = models.CharField(max_length=255, blank=True, null=True)
    expiring_soon = models.BooleanField(default=False)
    brand = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.item_name