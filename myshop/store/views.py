from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm()
    return render(request, 'store/product_detail.html', {'product': product, 'form': form})
