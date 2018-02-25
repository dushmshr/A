from django.contrib import admin
from .models import Product, Cash, Order,ProductAdmin,Order_Item,Order_ItemAdmin

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Cash)
admin.site.register(Order)
admin.site.register(Order_Item,Order_ItemAdmin)

