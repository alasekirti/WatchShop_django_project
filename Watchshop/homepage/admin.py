from django.contrib import admin
from .models import Watches, WatchesUploads, Wishlist, Cart, WatchReview, CartItem

# Register your models here.
admin.site.register(Watches)


#Wishlist
# class WishListAdmin(admin.ModelAdmin):
#     list_display = ('user', 'products')
#     list_filter = ('user', 'products')
admin.site.register(Wishlist)


# #Cart
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'products')
#     list_filter = ('user', 'products')
admin.site.register(Cart)
admin.site.register(CartItem)


#WatchUploads
class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image', 'count')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)

#WatchReview
class WatchReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'rating')
    list_filter = ('rating', 'product')
admin.site.register(WatchReview, WatchReviewAdmin)

# Register your models here.
