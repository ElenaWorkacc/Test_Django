from products.views import index, product
from django.urls import path


urlpatterns = [
    path('', index),
    path('items/', product),
    path('headproducts/', index)
]