# apps/orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from django.contrib.admin.views.decorators import staff_member_required
from catalog.models import Product

def order_create(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart.values():
                product = Product.objects.get(id=item['product_id'])
                OrderItem.objects.create(order=order, product=product, price=product.price, quantity=item['quantity'])
            request.session['cart'] = {}
            return redirect(reverse('order_created', args=[order.id]))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'form': form})

def order_created(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_created.html', {'order': order})

@staff_member_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

@staff_member_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

@staff_member_required
def change_order_status(request, order_id, status):
    order = get_object_or_404(Order, id=order_id)
    order.status = status
    order.save()
    return redirect('order_detail', order_id=order.id)
