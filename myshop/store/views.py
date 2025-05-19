from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

import os
from django.conf import settings

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm()
    return render(request, 'store/product_detail.html', {'product': product, 'form': form})




@login_required
def secure_download(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if user has purchased the product
    has_ordered = product.order_items.filter(order__email=request.user.email).exists()
    if not has_ordered:
        raise Http404("You have not purchased this product.")

    file_path = product.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response

    raise Http404("File not found.")
