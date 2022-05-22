from django.urls import path

from . import views

app_name = 'showcase'
urlpatterns = [
    path('', views.ItemsView.as_view(), name='items'),
    path('items/<int:pk>', views.ItemView.as_view(), name='item')
]