from django.urls import path
from . import views

urlpatterns = [
    path('',views.itemlist,name='list'),
    path('add-item',views.createItem,name='create-item'),
    path('view-item/<str:pk>',views.getItem,name='getitem'),
    path('item-delete/<str:pk>',views.deleteItem,name="deleteItem"),
    path('item-update/<str:pk>',views.updateItem,name="update")
]

