from django.contrib import admin

from .models import MainMenu, Book, Review, ShippingAddress, Order, OrderItem

# Register your models here.

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

