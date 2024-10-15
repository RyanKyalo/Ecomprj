from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from core.models import Product, Category, Vendor, CartOrder, Address, ProductImages, CartOrderItems, Wishlist, ProductReviews


def index(request):
    #products = Product.objects.all()
    products = Product.objects.filter(product_status="published", featured = True).order_by("-id")
    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)



def product_list_view(request):
    
    products = Product.objects.filter(product_status="published")
    context = {
        "products":products
    }
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)
    
def  category_product_list_view(request,cid):
        category = Category.object.get(cid=cid)
        prodects = Product.object.filter(product_status="published, category=category")
        
        context ={
            "category":category,
            "products":products,
        }
        
        return render(request, "core/category-product-list.html")