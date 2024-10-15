from core.models import Product, Category, Vendor, CartOrder, Address, ProductImages, CartOrderItems, Wishlist, ProductReviews


def default(request):
    categories = Category.objects.all()
    return {
        'categories':categories,
    }