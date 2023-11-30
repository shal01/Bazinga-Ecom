from django.urls import path
from . import views


urlpatterns = [
    path('',views.store,name='store'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart,name='cart'),
    path('update-cart/',views.update_cart,name='updatecart'),
    path('process-update/',views.processUpdate,name='process-update'),

]


