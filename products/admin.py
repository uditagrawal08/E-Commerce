from django.contrib import admin

# Register your models here.

from .models import Product, Category,ProductImage

admin.site.register(Category)
admin.site.register(ProductImage)

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]
    
admin.site.register(Product,ProductAdmin)

    