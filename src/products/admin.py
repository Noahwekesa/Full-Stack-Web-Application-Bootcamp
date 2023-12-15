from django.contrib import admin
from products.models import Product, Shirts

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "image", "brand", "category"]
    search_fields = ["title", "category", "brand"]


admin.site.register(Shirts)
admin.site.register(Product, ProductAdmin)
