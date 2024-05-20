from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'productId', 'productPrice', 'productRating', 'productHave', 'productBrand', 'productCategory')
    search_fields = ('productName', 'productId', 'productBrand', 'productCategory')
    list_filter = ('productBrand', 'productCategory', 'productHave')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'customerAddress', 'totalPrice', 'approved', 'orderDate')
    search_fields = ('customerName', 'customerAddress')
    list_filter = ('approved', 'orderDate')
    inlines = [OrderItemInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
