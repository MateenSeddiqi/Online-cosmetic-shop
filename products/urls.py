from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('displayFeedback/', views.displayFeedback, name='displayFeedback'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('products/', views.products, name='products'),
    # path('product/<int:product_id>/', views.product, name='product'),
    # path('cart/', views.cart, name='cart'),
]