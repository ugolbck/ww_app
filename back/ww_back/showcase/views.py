from django.shortcuts import render, get_object_or_404
from .models import Item
from django.views import generic


class ItemsView(generic.ListView):
    template_name = 'showcase/index.html'
    context_object_name = 'latest_items'

    def get_queryset(self):
        return Item.objects.order_by('-publication_date')[:5]


class ItemView(generic.DetailView):
    model = Item
    template_name = 'showcase/item.html'
