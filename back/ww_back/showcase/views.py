from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Item


def items(request):
    latest_items = Item.objects.order_by('-publication_date')[:5]
    context = {'latest_items': latest_items}
    return render(request, 'showcase/index.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'showcase/item.html', {'item': item})