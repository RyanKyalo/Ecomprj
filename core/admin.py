from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, Address, ProductImages, CartOrderItems, Wishlist, ProductReviews
from django import template

class ProductsImagesAdmin(admin.TabularInline): 
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImagesAdmin]
    list_display = ['user', 'title', 'product_image','category','vendor', 'price', 'featured', 'product_status']    
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']    
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','order_date', 'price', 'paid_status', 'product_status']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item',  'price', 'product_status', 'product_status', 'invoice_no', 'image', 'qty', 'price', 'total']
    
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
    