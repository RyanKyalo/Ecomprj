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
        products = Product.object.filter(product_status="published, category=category")
        
        context ={
            "category":category,
            "products":products,
        }
        
        return render(request, "core/category-product-list.html")
    
def vendor_list_view(request):
    vendor = Vendor.objects.all()
    context = {
        "vendor": vendor,
    }
    return render(request, "core/vendor-list.html", context)

def vendor_detail_view(request,vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor = vendor, product_status= "published")
    context = {
        "vendor": vendor,
        "products": products,
    }
    return render(request, "core/vendor-detail.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    
    p_image = product.p_image.all()
    
    context ={
        "p" : product,
        "p_image" : p_image,
        "products" : products,
    }
    return render (request, "core/product-detail.html", context)