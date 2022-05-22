from django.urls import path

from . import views

app_name = 'showcase'
urlpatterns = [
    path('', views.items, name='items'),
    path('items/<int:item_id>', views.item, name='item')
]