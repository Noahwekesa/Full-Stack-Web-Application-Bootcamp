from django.contrib import admin
from products.models import Product, Shirts

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "image", "brand", "category"]


admin.site.register(Shirts)
admin.site.register(Product, ProductAdmin)
