from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Item

def index(request):
    return render(request, 'index.html')


def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'item.html', {'item': item})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def category(request, category_name):
    items = Item.objects.filter(category = category_name)
    return render(request, 'items.html', {
        'products': items,
        'category_name': category_name
        })