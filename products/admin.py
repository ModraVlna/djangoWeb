from django.contrib import admin

# Register your models here.
from .models import Product #importing the class Product
admin.site.register(Product)


