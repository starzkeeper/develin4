from django.shortcuts import render, get_object_or_404
from electronic.models import Product



def index(request):
    products = Product.objects.all()
    return render(request,'vision/index.html',{'products':products})


def show_post(request, slug):
    post = get_object_or_404(Product, slug=slug)

    context = {
    'post': post,
    'title': post.name,
    'cat_selected': post.cat_id,
    }

    return render(request, 'vision/ProductDetailView.html', context=context)

