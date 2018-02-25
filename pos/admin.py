from django.contrib import admin
from .models import Product, Cash, Order,ProductAdmin,Order_Item,CashAdmin

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Cash,CashAdmin)
admin.site.register(Order)


