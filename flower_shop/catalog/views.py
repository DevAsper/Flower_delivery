from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'catalog/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalog/product_detail.html', {'product': product})

